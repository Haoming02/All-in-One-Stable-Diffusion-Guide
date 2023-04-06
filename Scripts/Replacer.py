import sys
import os

FOLDER = sys.argv[1]
BEFORE = sys.argv[2]
AFTER = sys.argv[3]

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    with open(FOLDER + '/' + FILE, 'r') as f:
        original_line = f.readlines()

    lines = original_line[0].replace(BEFORE, AFTER)

    tags = [word.strip() for word in lines.split(',')]
    while '' in tags:
        tags.remove('')
    line = ', '.join(tags)

    with open(FOLDER + '/' + FILE, 'w') as f:
        f.writelines(line)