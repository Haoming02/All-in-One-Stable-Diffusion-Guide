from Formatter import format, params, listdir


def append(folder: str, append: str):

    for FILE in listdir(folder, ".txt"):

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read()

        ap_tags = format(append)
        og_tags = [tag for tag in format(line) if tag not in ap_tags]

        line = ", ".join(og_tags + ap_tags)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":

    args = params(2, 2, ("path to folder", "tags"))
    append(*args)
