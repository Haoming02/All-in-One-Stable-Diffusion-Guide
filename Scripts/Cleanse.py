from Formatter import params, listdir


def cleanse(FOLDER: str):
    files = listdir(FOLDER, ".txt")

    for FILE in files:

        with open(FILE, "w", encoding="utf-8") as f:
            f.write("")


if __name__ == "__main__":
    import os

    (folder,) = params(1, 1, os.path.basename(__file__), ["path to folder"])

    cleanse(folder)
