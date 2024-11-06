from Formatter import params, listdir
import os


def generate(folder: str):
    for file in listdir(folder):
        if file.endswith(".txt"):
            continue

        filename = os.path.splitext(file)[0]
        caption = f"{filename}.txt"

        if os.path.isfile(caption):
            continue

        with open(caption, "w+", encoding="utf-8") as f:
            f.write("")


if __name__ == "__main__":

    args = params(1, 1, ("path to folder",))
    generate(*args)
