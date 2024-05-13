from Formatter import format, params, listdir


def append(FOLDER: str, APPEND: str):
    files = listdir(FOLDER, ".txt")

    for FILE in files:

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read()

        og_tags = format(line)
        ap_tags = format(APPEND)

        for tag in ap_tags:
            if tag in og_tags:
                og_tags.remove(tag)

        line = ", ".join(og_tags + ap_tags)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    import os

    folder, tag = params(2, 2, os.path.basename(__file__), ["path to folder", "tags"])

    append(folder, tag)
