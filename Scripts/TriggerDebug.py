from Formatter import Format
import os

def debug(FOLDER:str, index:int):
    for FILE in os.listdir(FOLDER):
        if '.txt' not in FILE:
            continue

        with open(os.path.join(FOLDER, FILE), 'r', encoding='utf-8') as f:
            lines = f.read().strip()

        tags = Format(lines)
        print(f'{FILE:<8}\t{tags[index]}')


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('\nUsage:\npython Priority.py "<path to folder>" <index>')
        raise SystemExit
    elif len(sys.argv) > 3:
        print('\nUse " " to encapsulate your paths and tags')
        raise SystemExit

    debug(sys.argv[1], int(sys.argv[2]))
