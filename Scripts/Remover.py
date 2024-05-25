from Formatter import format, params, listdir


def remove(FOLDER: str, REMOVE: str | int):
    files = listdir(FOLDER, ".txt")

    for FILE in files:

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read()

        try:
            rm_index = int(REMOVE)
            og_tags = format(line)
            og_tags.pop(rm_index)
            line = ", ".join(og_tags)

        except ValueError:
            og_tags = format(line)
            rm_tags = format(REMOVE)

            for tag in rm_tags:
                if tag in og_tags:
                    og_tags.remove(tag)

            line = ", ".join(og_tags)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    import os

    folder, tag = params(2, 2, os.path.basename(__file__), ["path to folder", "tags"])

    remove(folder, tag)
