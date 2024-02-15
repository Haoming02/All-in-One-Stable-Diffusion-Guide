from Formatter import Format
import os

def replace(FOLDER:str, SAUCE:str, TARGET:str):
    for FILE in os.listdir(FOLDER):
        if '.txt' not in FILE:
            continue

        if len(SAUCE.split(',')) > 1 or len(TARGET.split(',')) > 1:
            print('\nReplacer only works on 1 tag at a time')
            raise SystemExit

        if len(SAUCE) == 0:
            SAUCE = ' '
        if len(TARGET) == 0:
            TARGET = ' '

        with open(os.path.join(FOLDER, FILE), 'r', encoding='utf-8') as f:
            lines = f.read().strip()

        og_tags = Format(lines)
        dedupe = []

        for tag in og_tags:
            if tag not in dedupe:
                dedupe.append(tag.replace(SAUCE, TARGET))

        line = ', '.join(dedupe)

        with open(os.path.join(FOLDER, FILE), 'w') as f:
            f.write(line)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 4:
        print('\nUsage:\npython Replacer.py "<path to folder>" "<tags>" "<tags>"')
        raise SystemExit
    elif len(sys.argv) > 4:
        print('\nUse " " to encapsulate your paths and tags')
        raise SystemExit

    replace(sys.argv[1], sys.argv[2].strip(), sys.argv[3].strip())
