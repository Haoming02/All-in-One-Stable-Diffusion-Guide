from Formatter import format, params, listdir


def replace(folder: str, source: str, target: str):

    is_multiple = False

    if len(source.split(",")) > 1 or len(target.split(",")) > 1:
        source = ", ".join(format(source))
        target = ", ".join(format(target))
        is_multiple = True

    if len(source.strip()) == 0:
        source = " "

    if len(target.strip()) == 0:
        target = " "

    for file in listdir(folder, ".txt"):

        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        if is_multiple:
            og = ", ".join(format(line))
            line = og.replace(source, target)

        og_tags = format(line)
        dedupe = []

        for tag in og_tags:
            if not is_multiple:
                tag = tag.replace(source, target)
            if tag not in dedupe:
                dedupe.append(tag)

        line = ", ".join(dedupe)

        with open(file, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":

    args = params(3, 3, ("path to folder", "tag", "tag"))
    replace(*args)
