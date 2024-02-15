from Formatter import Format
import os

def clean(FOLDER:str, DEL_COLOR:bool):
	DELETE_TAGS = [
		'1girl', '1boy', 'solo', 'hair', 'bang', 'uniform', 'dress', 'shirt', 'skirt',
		'virtual', 'plaid', 'sleeve', 'short', 'long', '!', '?'
	]

	if DEL_COLOR:
		DELETE_TAGS += [
			'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'purple', 'white',
			'black', 'grey', 'gray', 'silver', 'pink', 'brown', 'teal', 'violet', 'aqua'
		]

	for FILE in os.listdir(FOLDER):
		if '.txt' not in FILE:
			continue

		with open(os.path.join(FOLDER, FILE), 'r', encoding='utf-8') as f:
			lines = f.read().strip()

		tags = Format(lines)
		cleaned_tags = []

		for tag in tags:
			if not any(to_d in tag for to_d in DELETE_TAGS):
				cleaned_tags.append(tag)

		line = ', '.join(cleaned_tags)

		with open(os.path.join(FOLDER, FILE), 'w') as f:
			f.write(line)


if __name__ == '__main__':
	import sys

	if len(sys.argv) < 2:
		print('\nUsage:\npython CleanTags.py "<path to folder>"')
		raise SystemExit
	elif len(sys.argv) > 3:
		print('\nUse " " to encapsulate your paths')
		raise SystemExit

	FOLDER = sys.argv[1]
	DEL_COLOR = False if len(sys.argv) < 3 else bool(sys.argv[2].strip())

	clean(FOLDER, DEL_COLOR)
