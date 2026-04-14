#!/usr/bin/env bash
set -euo pipefail

CSV_FILE="$1"
OUT_DIR="${2:-.}"

mkdir -p "$OUT_DIR"
BASE_NAME="$(basename "$CSV_FILE" .csv)"

ruby -rcsv -rjson -e '
csv_file = ARGV[0]
out_dir = ARGV[1]
base_name = ARGV[2]

lines = File.readlines(csv_file, chomp: true)

header_idx = lines.find_index { |l| l.start_with?("Rank,") }
abort("Fehler: Header-Zeile mit Rank,... nicht gefunden") unless header_idx

header = CSV.parse_line(lines[header_idx])
data_lines = lines[(header_idx + 1)..] || []

species_idx = header.index("Species")
sf_idx = header.index("SF%")

abort("Fehler: Spalte Species nicht gefunden") unless species_idx
abort("Fehler: Spalte SF% nicht gefunden") unless sf_idx

pretty_name = base_name.split("_").map(&:capitalize).join(" ")

rows = data_lines.filter_map do |line|
  next if line.strip.empty?

  row = CSV.parse_line(line) rescue next
  next unless row && row.length > [species_idx, sf_idx].max

  species_raw = row[species_idx].to_s.strip
  sf_raw = row[sf_idx].to_s.strip

  next if species_raw.empty? || sf_raw.empty?

  scientific_name = species_raw.split(",").first.to_s.strip
  next if scientific_name.empty?

  # nur saubere binomiale Namen
  next unless scientific_name.match?(/\A[A-Z][a-z]+ [a-z][a-z-]+\z/)

  sf = sf_raw.to_f
  { name: scientific_name, sf: sf }
end

# doppelte Namen entfernen, höchste SF behalten
rows = rows
  .group_by { |r| r[:name] }
  .map { |_name, group| group.max_by { |r| r[:sf] } }

# nach SF absteigend, bei Gleichstand alphabetisch
sorted = rows.sort_by { |r| [-r[:sf], r[:name]] }

n = sorted.length
abort("Fehler: Keine gültigen Arten gefunden") if n == 0

# Prozentuale Zielgrößen
target_l1 = (n * 0.2).ceil
target_l2 = (n * 0.3).ceil

# Mindestgrößen
min_l1 = 15
min_l2 = 15

if n >= 40
  l1_size = [target_l1, min_l1].max
  l2_size = [target_l2, min_l2].max

  # Nicht mehr vergeben als vorhanden
  l1_size = [l1_size, n].min
  l2_size = [l2_size, n - l1_size].min
else
  # Für kleine Datensätze fixer, robuster Split
  l1_size = [10, n].min
  l2_size = [10, n - l1_size].min
end

level1 = sorted[0, l1_size] || []
level2 = sorted[l1_size, l2_size] || []
level3 = sorted[(l1_size + l2_size)..] || []

levels = {
  "level1" => {
    "name" => "#{pretty_name} - Level 1",
    "description" => "Sehr häufige Arten",
    "speciesNames" => level1.map { |r| r[:name] }
  },
  "level2" => {
    "name" => "#{pretty_name} - Level 2",
    "description" => "Häufige Arten",
    "speciesNames" => level2.map { |r| r[:name] }
  },
  "level3" => {
    "name" => "#{pretty_name} - Level 3",
    "description" => "Seltene Arten",
    "speciesNames" => level3.map { |r| r[:name] }
  }
}

levels.each do |level, payload|
  payload["imageUrl"] = ""
  payload["sources"] = [
    {
      "name" => "REEF",
      "url" => "https://www.reef.org/"
    }
  ]
  out_file = File.join(out_dir, "#{base_name}_#{level}.json")
  File.write(out_file, JSON.pretty_generate(payload))
  puts "geschrieben: #{out_file}"
end

puts
puts "Gesamtarten: #{n}"
puts "Level 1: #{level1.length}"
puts "Level 2: #{level2.length}"
puts "Level 3: #{level3.length}"
' "$CSV_FILE" "$OUT_DIR" "$BASE_NAME"