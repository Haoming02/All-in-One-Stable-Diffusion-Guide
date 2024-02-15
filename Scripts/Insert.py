from Formatter import Format
import os

def insert(FOLDER:str, INSERT:str):
    for FILE in os.listdir(FOLDER):
        if '.txt' not in FILE:
            continue

        with open(os.path.join(FOLDER, FILE), 'r', encoding='utf-8') as f:
            lines = f.read().strip()

        og_tags = Format(lines)
        in_tags = Format(INSERT)

        for tag in in_tags:
            if tag in og_tags:
                og_tags.remove(tag)

        line = ', '.join(in_tags + og_tags)

        with open(os.path.join(FOLDER, FILE), 'w') as f:
            f.write(line)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('\nUsage:\npython Insert.py "<path to folder>" "<tags>"')
        raise SystemExit
    elif len(sys.argv) > 3:
        print('\nUse " " to encapsulate your paths and tags')
        raise SystemExit

    insert(sys.argv[1], sys.argv[2])
