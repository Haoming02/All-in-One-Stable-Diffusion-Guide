from Formatter import format, params, listdir


def replace(folder: str, source: str, target: str):
    source, target = int(source), int(target)

    for file in listdir(folder, ".txt"):
        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        tags = format(line)
        tags[source], tags[target] = tags[target], tags[source]

        line = ", ".join(tags)

        with open(file, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    args = params(3, 3, ("path to folder", "from", "to"))
    replace(*args)
