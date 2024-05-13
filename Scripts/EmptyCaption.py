from Formatter import params, listdir
import os

def generate(FOLDER: str):
    files = listdir(FOLDER)

    for FILE in files:
        if FILE.endswith(".txt"):
            continue

        filename = os.path.splitext(FILE)[0]
        caption = f"{filename}.txt"

        if os.path.exists(caption):
            continue

        with open(caption, "w+", encoding="utf-8") as f:
            f.write("")


if __name__ == "__main__":

    (folder,) = params(1, 1, os.path.basename(__file__), ["path to folder"])

    generate(folder)
