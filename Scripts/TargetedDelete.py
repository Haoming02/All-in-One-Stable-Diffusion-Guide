from Formatter import format, params, listdir
import os


def delete(path: str, filter: str):
    for FILE in listdir(path, ".txt"):

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read()

        og_tags = format(line)

        if filter in og_tags:
            os.remove(FILE)

            for fmt in (".png", ".jpg", ".jpeg"):
                try:
                    os.remove(FILE.replace(".txt", fmt))
                except FileNotFoundError:
                    pass


if __name__ == "__main__":

    args = params(2, 2, ("path to folder", "tag"))
    delete(*args)
