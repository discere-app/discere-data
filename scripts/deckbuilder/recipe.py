# =============================================================================
# recipe.py — read a recipe and check it against schema/recipe.schema.json
#
# The recipe schema takes the deck texts and learning settings from
# schema/deck.schema.json by reference, so both are loaded into one
# registry; nothing is fetched from the network. Relative paths in the
# recipe (REEF CSV, guides) are resolved against the recipe's directory.
# =============================================================================

import json
import os

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

SCHEMA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "schema")


class RecipeError(Exception):
    pass


def _schema(name):
    with open(os.path.join(SCHEMA_DIR, name), encoding="utf-8") as f:
        return json.load(f)


def validator():
    recipe_schema = _schema("recipe.schema.json")
    deck_schema = _schema("deck.schema.json")
    registry = Registry().with_resources([
        (s["$id"], Resource.from_contents(s)) for s in (recipe_schema, deck_schema)
    ])
    return Draft202012Validator(recipe_schema, registry=registry, format_checker=FormatChecker())


def highlight_names(recipe):
    """The scientific names of the recipe's highlights, in recipe order."""
    return [h["name"] for h in recipe.get("highlights", [])]


def exclude_names(recipe):
    """The scientific names the recipe excludes by hand."""
    return [e["name"] for e in recipe.get("exclude", [])]


def placement_names(recipe):
    """The scientific names the recipe puts on a level by hand."""
    return [p["name"] for p in recipe.get("placements", [])]


def load(path):
    """The recipe at `path`, checked, with its file paths made absolute."""
    try:
        with open(path, encoding="utf-8") as f:
            recipe = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        raise RecipeError(f"{path}: {e}") from e
    errors = sorted(validator().iter_errors(recipe), key=lambda e: list(e.absolute_path))
    if errors:
        lines = [f"  {'/'.join(map(str, e.absolute_path)) or '(Wurzel)'}: {e.message}" for e in errors]
        raise RecipeError(f"{path} passt nicht zu schema/recipe.schema.json:\n" + "\n".join(lines))
    if len(recipe.get("levelMinCounts", [])) > len(recipe["levelSizes"]):
        raise RecipeError(f"{path}: levelMinCounts hat mehr Einträge als levelSizes")
    beyond = [p["name"] for p in recipe.get("placements", []) if p["level"] > len(recipe["levelSizes"])]
    if beyond:
        raise RecipeError(f"{path}: placements auf ein Level, das levelSizes nicht hat: " + ", ".join(beyond))
    base = os.path.dirname(os.path.abspath(path))
    if recipe["order"]["source"] == "reef":
        recipe["order"]["csv"] = os.path.join(base, recipe["order"]["csv"])
    for guide in recipe.get("guides", []):
        guide["path"] = os.path.join(base, guide["path"])
    return recipe
