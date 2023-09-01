from Formatter import Format
import sys
import os

FOLDER = sys.argv[1]
APPEND = sys.argv[2]
FILTER = None if len(sys.argv) < 4 else sys.argv[3]

if len(sys.argv) > 4:
    print('Too many inputs detected. Use " " to encapsulate your tags!')
    raise SystemExit

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    if FILTER:
        if FILTER not in FILE:
            continue

    with open(FOLDER + '/' + FILE, 'r') as f:
        lines = f.readlines()

    og_tags = Format(lines[0])
    ap_tags = Format(APPEND)

    for tag in ap_tags:
        if tag in og_tags:
            og_tags.remove(tag)

    line = ', '.join(og_tags)
    AP = ', '.join(ap_tags)

    with open(FOLDER + '/' + FILE, 'w') as f:
        f.writelines(line + ', ' + AP)
