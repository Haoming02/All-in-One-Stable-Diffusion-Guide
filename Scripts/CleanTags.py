import random
import sys
import os

FOLDER = sys.argv[1]
DEL_COLOR = False if len(sys.argv) < 3 else bool(sys.argv[2])

DELETE_TAGS = ['hair', 'bangs', 'uniform', 'shirt', 'skirt', 'virtual', 'plaid', 'sleeve', 'side_up', '!', '?']
COLORS_TAGS = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'purple', 'white', 'black', 'grey', 'silver', 'pink', 'brown', 'teal', 'violet']

if DEL_COLOR:
	DELETE_TAGS = DELETE_TAGS + COLORS_TAGS

for FILE in os.listdir(FOLDER):
	if '.txt' not in FILE:
		continue

	with open(FOLDER + '/' + FILE, "r") as f:
		lines = f.readlines()

	tags = [word.strip() for word in lines[0].split(',')]
	while '' in tags:
		tags.remove('')

	new_tags = []
	for tag in tags:
		if not any(td in tag for td in DELETE_TAGS):
			new_tags.append(tag)

	line = ', '.join(new_tags)

	with open(FOLDER + '/' + FILE, "w") as f:
		f.write(line)