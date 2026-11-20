# =============================================================================
# fetch.py — polite, cached HTTP GET for JSON APIs
#
# iNaturalist, GBIF and OBIS are public services that ask for restraint, and a
# recipe is run again and again while a deck takes shape. So every JSON
# response is kept in a cache outside the repository
# (~/.cache/discere-deckbuilder/http by default) and a repeated run reads it
# from there; --refresh fetches anew and overwrites the cache. Between two
# network requests to the same host the fetcher waits (1.2 s by default,
# what iNaturalist asks for), and every request carries its own User-Agent.
#
# The source modules take a fetcher as an argument and call only get_json,
# so the tests hand them a fake fetcher with recorded answers instead.
# =============================================================================

import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "discere-deckbuilder/1 (+https://github.com/discere-app/discere-data)"

# Seconds between two network requests to the same host.
DEFAULT_DELAY = 1.2

# Attempts per request; a 429 or 5xx is retried after a growing pause.
ATTEMPTS = 4


def build_url(base, params):
    """`base` with `params` as query; a list value repeats the parameter,
    and the parameters are sorted, so the same query gives the same URL and
    hence the same cache entry."""
    pairs = []
    for key in sorted(params):
        value = params[key]
        for item in value if isinstance(value, (list, tuple)) else [value]:
            pairs.append((key, str(item)))
    return f"{base}?{urllib.parse.urlencode(pairs)}" if pairs else base


class CachedFetcher:
    def __init__(self, cache_dir, refresh=False, delay=DEFAULT_DELAY):
        self.cache_dir = cache_dir
        self.refresh = refresh
        self.delay = delay
        self.network_requests = 0
        self.cache_hits = 0
        self._last_request = {}
        # With --refresh, each URL is fetched once per run and read from the
        # cache after that, like any other repeated query of the run.
        self._refreshed = set()

    def _cache_path(self, url):
        digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
        return os.path.join(self.cache_dir, digest[:2], f"{digest}.json")

    def get_json(self, base, params=None):
        url = build_url(base, params or {})
        path = self._cache_path(url)
        if os.path.exists(path) and (not self.refresh or url in self._refreshed):
            self.cache_hits += 1
            with open(path, encoding="utf-8") as f:
                return json.load(f)["body"]
        body = self._download(url)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = f"{path}.tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump({"url": url, "body": body}, f)
        os.replace(tmp, path)
        self._refreshed.add(url)
        return body

    def _wait_for(self, host):
        last = self._last_request.get(host)
        if last is not None:
            pause = self.delay - (time.monotonic() - last)
            if pause > 0:
                time.sleep(pause)
        self._last_request[host] = time.monotonic()

    def _download(self, url):
        host = urllib.parse.urlsplit(url).netloc
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        for attempt in range(1, ATTEMPTS + 1):
            self._wait_for(host)
            self.network_requests += 1
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    return json.load(response)
            except urllib.error.HTTPError as e:
                if attempt == ATTEMPTS or not (e.code == 429 or e.code >= 500):
                    raise RuntimeError(f"HTTP {e.code} für {url}") from e
            except urllib.error.URLError as e:
                if attempt == ATTEMPTS:
                    raise RuntimeError(f"keine Verbindung für {url}: {e.reason}") from e
            time.sleep(self.delay * 2 ** attempt)
