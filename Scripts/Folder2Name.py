from Formatter import format, params, listdir
import os


def insert(folder: str):
    for file in listdir(folder, ".txt"):
        path = os.path.basename(os.path.dirname(file))
        name = path.split("_", 1)[1].strip()

        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        og_tags = format(line)
        if name in og_tags:
            og_tags.remove(name)

        line = ", ".join([name, *og_tags])

        with open(file, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    args = params(1, 1, ("path to folder",))
    insert(*args)
