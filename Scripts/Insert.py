from Formatter import format, params, listdir


def insert(FOLDER: str, INSERT: str):
    files = listdir(FOLDER, ".txt")

    for FILE in files:

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read()

        og_tags = format(line)
        in_tags = format(INSERT)

        for tag in in_tags:
            if tag in og_tags:
                og_tags.remove(tag)

        line = ", ".join(in_tags + og_tags)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    import os

    folder, tag = params(2, 2, os.path.basename(__file__), ["path to folder", "tags"])

    insert(folder, tag)
