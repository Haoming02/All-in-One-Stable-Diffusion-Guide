from Formatter import format, params, listdir


def switch_order(folder: str):

    for FILE in listdir(folder, ".txt"):

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read()

        og_tags = format(line)
        tags = og_tags[1:] + [og_tags[0]]

        line = ", ".join(tags)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":

    args = params(1, 1, ("path to folder",))
    switch_order(*args)
