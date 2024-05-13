from Formatter import format, params, listdir


def replace(FOLDER: str, SAUCE: str, TARGET: str):
    files = listdir(FOLDER, ".txt")

    for FILE in files:

        if len(SAUCE.split(",")) > 1 or len(TARGET.split(",")) > 1:
            print("\n[Error] Replacer only works on 1 tag at a time...")
            raise SystemExit

        if len(SAUCE) == 0:
            SAUCE = " "

        if len(TARGET) == 0:
            TARGET = " "

        with open(FILE, "r", encoding="utf-8") as f:
            lines = f.read()

        og_tags = format(lines)
        dedupe = []

        for tag in og_tags:
            new = tag.replace(SAUCE, TARGET)
            if new not in dedupe:
                dedupe.append(new)

        line = ", ".join(dedupe)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    import os

    folder, fr, to = params(
        3, 3, os.path.basename(__file__), ["path to folder", "tags", "tags"]
    )

    replace(folder, fr.strip(), to.strip())
