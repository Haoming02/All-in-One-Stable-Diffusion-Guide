from Formatter import format, params, listdir


def debug(FOLDER: str, index: str | int):

    index = int(index)
    files = list(listdir(FOLDER, ".txt"))
    max_width = max(len(filename) for filename in files)

    print("")
    for file in files:

        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        tags = format(line)
        print(f"{file:<{max_width + 4}} {tags[index]}")


if __name__ == "__main__":

    args = params(2, 2, ("path to folder", "index"))
    debug(*args)
