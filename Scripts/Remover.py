from Formatter import Format
import os

def remove(FOLDER:str, REMOVE:str):
    for FILE in os.listdir(FOLDER):
        if '.txt' not in FILE:
            continue

        with open(os.path.join(FOLDER, FILE), 'r', encoding='utf-8') as f:
            lines = f.read().strip()

        og_tags = Format(lines)
        rm_tags = Format(REMOVE)

        for tag in rm_tags:
            if tag in og_tags:
                og_tags.remove(tag)

        line = ', '.join(og_tags)

        with open(os.path.join(FOLDER, FILE), 'w') as f:
            f.write(line)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('\nUsage:\npython Remover.py "<path to folder>" "<tags>"')
        raise SystemExit
    elif len(sys.argv) > 3:
        print('\nUse " " to encapsulate your paths and tags')
        raise SystemExit

    remove(sys.argv[1], sys.argv[2])
