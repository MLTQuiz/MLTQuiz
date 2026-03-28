import os
import re
from collections import defaultdict

# Folder to scan
folder = "."

# Output file
output_file = "prefix_counts.txt"

# Regex: prefix + trailing number + extension
pattern = re.compile(r"^(.*?)(\d+)(\.[^.]+)$")

counts = defaultdict(int)

for filename in os.listdir(folder):
    match = pattern.match(filename)
    if match:
        prefix = match.group(1)
        counts[prefix] += 1

# Write results to file
with open(output_file, "w") as f:
    for prefix, count in sorted(counts.items()):
        line = f"{prefix}: {count} files\n"
        f.write(line)
        print(line.strip())  # optional: also print to console