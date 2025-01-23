from Formatter import format, params, listdir


def remove(folder: str, remove: str):
    for file in listdir(folder, ".txt"):
        with open(file, "r", encoding="utf-8") as f:
            line = f.read()
            og_tags = format(line)

        if remove.isdecimal():
            rm_index = int(remove)
            if rm_index < len(og_tags):
                og_tags.pop(rm_index)

        else:
            rm_tags = format(remove)
            og_tags = [tag for tag in og_tags if tag not in rm_tags]

        line = ", ".join(og_tags)
        with open(file, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    args = params(2, 2, ("path to folder", "tags"))
    remove(*args)
