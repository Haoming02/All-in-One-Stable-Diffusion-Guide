from Formatter import params, listdir


def replace(folder: str, source: str, target: str):
    for file in listdir(folder, ".txt"):

        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        line = line.replace(source, target)

        with open(file, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":

    args = params(3, 3, ("path to folder", "tag", "tag"))
    replace(*args)
