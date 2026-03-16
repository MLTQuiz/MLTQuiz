import os
import json
import re
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
JSON_FILE = os.path.join(BASE_DIR, "imageDatabase.json")

# matches filenames like Pelger_Huet01.png
pattern = re.compile(r"^(.*?)(\d{2})\.[^.]+$")

# load json
with open(JSON_FILE, "r") as f:
    data = json.load(f)

# scan category folders inside images/
for folder in os.listdir(IMAGE_DIR):
    folder_path = os.path.join(IMAGE_DIR, folder)

    if not os.path.isdir(folder_path):
        continue

    if folder not in data:
        print(f"Skipping {folder} (not in JSON)")
        continue

    counts = defaultdict(int)

    for file in os.listdir(folder_path):
        match = pattern.match(file)
        if match:
            prefix = match.group(1)
            counts[prefix] += 1

    # update json section
    for prefix, count in counts.items():
        data[folder][prefix] = count

# write updated json
with open(JSON_FILE, "w") as f:
    json.dump(data, f, indent=2)

print("imageDatabase.json successfully updated.")