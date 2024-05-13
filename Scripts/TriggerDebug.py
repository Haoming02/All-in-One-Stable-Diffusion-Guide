from Formatter import format, params, listdir


def debug(FOLDER: str, index: int):
    files = listdir(FOLDER, ".txt")

    for FILE in files:

        with open(FILE, "r", encoding="utf-8") as f:
            lines = f.read()

        tags = format(lines)
        print(f"{FILE:<8}\t{tags[index]}")


if __name__ == "__main__":
    import os

    folder, index = params(
        2, 2, os.path.basename(__file__), ["path to folder", "index"]
    )

    debug(folder, int(index))
