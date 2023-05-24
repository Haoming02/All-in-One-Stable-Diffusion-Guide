from Formatter import Format
import sys
import os

FOLDER = sys.argv[1]
BEFORE = sys.argv[2]
AFTERR = sys.argv[3]

if len(sys.argv) > 4:
    print('Too many inputs detected. Use " " to encapsulate your tags!')
    exit()

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    with open(FOLDER + '/' + FILE, 'r') as f:
        original_line = f.readlines()

    line = original_line[0].replace(BEFORE.strip(), AFTERR.strip())

    tags = Format(line)

    line = ', '.join(tags)

    with open(FOLDER + '/' + FILE, 'w') as f:
        f.writelines(line)