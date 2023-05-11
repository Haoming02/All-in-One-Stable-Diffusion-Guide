import sys
import os

FOLDER = sys.argv[1]

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    with open(FOLDER + '/' + FILE, 'r') as f:
        original_line = f.readlines()

    tags = [word.strip() for word in original_line[0].split(',')]
    while '' in tags:
        tags.remove('')

    dedupe = []

    for tag in tags:
        if tag not in dedupe:
            dedupe.append(tag)

    line = ', '.join(dedupe)

    with open(FOLDER + '/' + FILE, 'w') as f:
        f.writelines(line)