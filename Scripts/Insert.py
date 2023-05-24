from Formatter import Format
import sys
import os

FOLDER = sys.argv[1]
INSERT = sys.argv[2]
FILTER = None if len(sys.argv) < 4 else sys.argv[3]

if len(sys.argv) > 4:
    print('Too many inputs detected. Use " " to encapsulate your tags!')
    exit()

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    if FILTER:
        if FILTER not in FILE:
            continue

    with open(FOLDER + '/' + FILE, 'r') as f:
        lines = f.readlines()

    og_tags = Format(lines[0])
    in_tags = Format(INSERT)

    for tag in in_tags:
        if tag in og_tags:
            og_tags.remove(tag)

    line = ', '.join(og_tags)
    IN = ', '.join(in_tags)

    with open(FOLDER + '/' + FILE, 'w') as f:
        f.writelines(IN + ', ' + line)