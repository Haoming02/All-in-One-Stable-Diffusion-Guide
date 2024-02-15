def Format(input_string:str) -> list:
	tags = [word.strip() for word in input_string.split(',')]
	while '' in tags:
		tags.remove('')

	return tags


if __name__ == '__main__':
    import sys
    import os

    if len(sys.argv) < 2:
        print('\nUsage:\npython Formatter.py "<path to folder>"')
        raise SystemExit
    elif len(sys.argv) > 2:
        print('\nUse " " to encapsulate your path')
        raise SystemExit

    FOLDER = sys.argv[1].strip('"').strip()

    for FILE in os.listdir(FOLDER):
        if '.txt' not in FILE:
            continue

        with open(os.path.join(FOLDER, FILE), 'r', encoding='utf-8') as f:
            original_line = f.read().strip()

        tags = Format(original_line)
        dedupe = []

        for tag in tags:
            if tag not in dedupe:
                dedupe.append(tag)

        line = ', '.join(dedupe)

        with open(os.path.join(FOLDER, FILE), 'w') as f:
            f.write(line)
