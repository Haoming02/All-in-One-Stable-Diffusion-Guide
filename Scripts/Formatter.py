import sys
import os

def Format(input_string):
	tags = [word.strip() for word in input_string.split(',')]
	while '' in tags:
		tags.remove('')

	return tags

def main():
    FOLDER = sys.argv[1]

    for FILE in os.listdir(FOLDER):
        if '.txt' not in FILE:
            continue

        with open(FOLDER + '/' + FILE, 'r') as f:
            original_line = f.readlines()

        tags = Format(original_line[0])

        dedupe = []

        for tag in tags:
            if tag not in dedupe:
                dedupe.append(tag)

        line = ', '.join(dedupe)

        with open(FOLDER + '/' + FILE, 'w') as f:
            f.writelines(line)

if __name__ == '__main__':
    main()