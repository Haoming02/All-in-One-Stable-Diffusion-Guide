from pathlib import Path
import sys
import os

FOLDER = sys.argv[1]
INSERT = sys.argv[2]

SNAPSHOT = os.listdir(FOLDER)

for FILE in SNAPSHOT:
    if '.txt' in FILE:
        continue

    FileName = Path(FILE).stem

    with open(FOLDER + '/' + FileName + '.txt', 'w') as f:
        f.write(INSERT)