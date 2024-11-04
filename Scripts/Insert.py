from Formatter import format, params, listdir


def insert(folder: str, insert: str, index: None | int | str = None):

    index = int(index) if index is not None else 0

    for file in listdir(folder, ".txt"):

        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        in_tags = format(insert)
        og_tags = [tag for tag in format(line) if tag not in in_tags]

        line = ", ".join(og_tags[:index] + in_tags + og_tags[index:])

        with open(file, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":

    args = params(2, 3, ("path to folder", "tags", "index"))
    insert(*args)
