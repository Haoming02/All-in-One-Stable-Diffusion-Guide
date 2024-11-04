from Formatter import format, params, listdir


def remove(folder: str, remove: str | int):

    for file in listdir(folder, ".txt"):

        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        try:
            rm_index = int(remove)
            og_tags = format(line)
            if rm_index < len(og_tags):
                og_tags.pop(rm_index)
            line = ", ".join(og_tags)

        except ValueError:
            rm_tags = format(remove)
            og_tags = [tag for tag in format(line) if tag not in rm_tags]
            line = ", ".join(og_tags)

        with open(file, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":

    args = params(2, 2, ("path to folder", "tags"))
    remove(*args)
