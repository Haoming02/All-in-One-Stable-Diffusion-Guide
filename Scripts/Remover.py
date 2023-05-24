from Formatter import Format
import sys
import os

FOLDER = sys.argv[1]
REMOVE = sys.argv[2]

if len(sys.argv) > 3:
    print('Too many inputs detected. Use " " to encapsulate your tags!')
    exit()

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    with open(FOLDER + '/' + FILE, 'r') as f:
        lines = f.readlines()

    og_tags = Format(lines[0])
    rm_tags = Format(REMOVE)

    for tag in rm_tags:
        if tag in og_tags:
            og_tags.remove(tag)

    line = ', '.join(og_tags)

    with open(FOLDER + '/' + FILE, 'w') as f:
        f.writelines(line)