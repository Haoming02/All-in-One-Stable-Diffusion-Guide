from Formatter import format, params, listdir
import os


def insert(folder: str):

    for FILE in listdir(folder, ".txt"):
        path = os.path.basename(os.path.dirname(FILE))
        name = path.split("_", 1)[1].strip()

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read()

        og_tags = format(line)
        if name in og_tags:
            og_tags.remove(name)

        line = ", ".join([name] + og_tags)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":

    args = params(1, 1, ("path to folder",))
    insert(*args)
