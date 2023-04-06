import sys
import os

FOLDER = sys.argv[1]
INSERT = sys.argv[2]

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    with open(FOLDER + '/' + FILE, 'r') as f:
        lines = f.readlines()

    tags = [word.strip() for word in lines[0].split(',')]
    while '' in tags:
        tags.remove('')
    line = ', '.join(tags)

    tag = [word.strip() for word in INSERT.split(',')]
    while '' in tag:
        tag.remove('')
    IN = ', '.join(tag)

    with open(FOLDER + '/' + FILE, 'w') as f:
        f.writelines(line + ', ' + IN)