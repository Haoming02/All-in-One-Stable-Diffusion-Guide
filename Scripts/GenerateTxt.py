from Formatter import Format
from pathlib import Path
import sys
import os

FOLDER = sys.argv[1]
INSERT = sys.argv[2]

if len(sys.argv) > 3:
    print('Too many inputs detected. Use " " to encapsulate your tags!')
    raise SystemExit

SNAPSHOT = os.listdir(FOLDER)

for FILE in SNAPSHOT:
    if '.txt' in FILE:
        continue

    FileName = Path(FILE).stem

    tags = Format(INSERT)
    line = ', '.join(tags)

    with open(FOLDER + '/' + FileName + '.txt', 'w') as f:
        f.write(line)
