import os
import re

# Set the path to your log files
log_folder = r"C:\Users\Administrator\Downloads\logs_craze"  # ← UPDATE this if needed

kills = 0
deaths = 0

name = "Daniel Burke"

# Compile regex patterns
kill_pattern = re.compile(fr"\b{name} has killed\b", re.IGNORECASE)
death_pattern = re.compile(fr"has killed\s+\[.*?\]{name}", re.IGNORECASE)

# Scan all files
for filename in os.listdir(log_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(log_folder, filename), 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if kill_pattern.search(line):
                    kills += 1
                elif death_pattern.search(line):
                    deaths += 1

# Show results
if deaths == 0:
    kd_ratio = float('inf')
else:
    kd_ratio = kills / deaths

print(f"Kills: {kills}")
print(f"Deaths: {deaths}")
print(f"Kill/Death Ratio: {kd_ratio:.2f}" if kd_ratio != float('inf') else "Kill/Death Ratio: ∞ (no deaths)")
