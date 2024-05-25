from Formatter import format, params, listdir


def replace(FOLDER: str, SAUCE: str, TARGET: str):
    files = listdir(FOLDER, ".txt")

    FLAG_multiple = False

    if len(SAUCE.split(",")) > 1 or len(TARGET.split(",")) > 1:
        SAUCE = ", ".join(format(SAUCE))
        TARGET = ", ".join(format(TARGET))
        FLAG_multiple = True

    if len(SAUCE.strip()) == 0:
        SAUCE = " "

    if len(TARGET.strip()) == 0:
        TARGET = " "

    for FILE in files:

        with open(FILE, "r", encoding="utf-8") as f:
            lines = f.read()

        if FLAG_multiple:
            og = ", ".join(format(lines))
            line = og.replace(SAUCE, TARGET)
            og_tags = format(line)
        else:
            og_tags = format(lines)

        dedupe = []

        for tag in og_tags:
            if not FLAG_multiple:
                tag = tag.replace(SAUCE, TARGET)
            if tag not in dedupe:
                dedupe.append(tag)

        line = ", ".join(dedupe)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    import os

    folder, fr, to = params(
        3, 3, os.path.basename(__file__), ["path to folder", "tags", "tags"]
    )

    replace(folder, fr.strip(), to.strip())
