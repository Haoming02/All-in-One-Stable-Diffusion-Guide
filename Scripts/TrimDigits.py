import sys
import os

FOLDER = sys.argv[1]

# 00001-0-FILENAME.txt
LEN = 8

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    os.rename(FOLDER + '/' + FILE, FOLDER + '/' + FILE[LEN:])