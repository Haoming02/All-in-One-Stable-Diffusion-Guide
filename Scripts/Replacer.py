import sys
import os

FOLDER = sys.argv[1]
BEFORE = sys.argv[2]
AFTER = sys.argv[3]

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    with open(FOLDER + '/' + FILE, 'r', encoding="utf-8") as f:
        original_line = f.readlines()

    tags = [word.strip() for word in original_line[0].split(',')]
    line = ', '.join(tags)

    new_line = line.replace(BEFORE, AFTER)

    with open(FOLDER + '/' + FILE, 'w') as f:
        f.writelines(new_line)