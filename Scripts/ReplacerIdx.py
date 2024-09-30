from Formatter import format, params, listdir


def replace(folder: str, source: str, target: str):
    source, target = int(source), int(target)

    for FILE in listdir(folder, ".txt"):

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read()

        tags = format(line)

        tags[source], tags[target] = tags[target], tags[source]

        line = ", ".join(tags)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":

    args = params(3, 3, ("path to folder", "from", "to"))
    replace(*args)
