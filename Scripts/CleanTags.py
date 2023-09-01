from Formatter import Format
import sys
import os

FOLDER = sys.argv[1]
DEL_COLOR = False if len(sys.argv) < 3 else bool(sys.argv[2])

DELETE_TAGS = ['hair', 'bang', 'uniform', 'shirt', 'skirt', 'virtual', 'plaid', 'sleeve', 'side_up', 'short', 'long', '!', '?']
COLORS_TAGS = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'purple', 'white', 'black', 'grey', 'gray', 'silver', 'pink', 'brown', 'teal', 'violet']

if DEL_COLOR:
	DELETE_TAGS = DELETE_TAGS + COLORS_TAGS

for FILE in os.listdir(FOLDER):
	if '.txt' not in FILE:
		continue

	with open(FOLDER + '/' + FILE, "r") as f:
		lines = f.readlines()

	tags = Format(lines[0])

	cleaned_tags = []

	for tag in tags:
		if not any(td in tag for td in DELETE_TAGS):
			cleaned_tags.append(tag)

	line = ', '.join(cleaned_tags)

	with open(FOLDER + '/' + FILE, "w") as f:
		f.write(line)
