from Formatter import format, params, listdir

COLORS: tuple[str] = (
    "aqua",
    "black",
    "blonde",
    "blue",
    "brown",
    "cyan",
    "light",
    "green",
    "grey",
    "orange",
    "pink",
    "purple",
    "lavender",
    "red",
    "silver",
    "white",
    "yellow",
    "violet",
)


def prune(folder: str):

    for FILE in listdir(folder, ".txt"):

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read()

        og_tags = format(line)
        pruned_tags = []

        for tag in og_tags:
            if ("hair" not in tag) and ("eye" not in tag):
                pruned_tags.append(tag)
                continue

            objs = tag.rsplit(" ", 1)
            if len(objs) == 1:
                objs = tag.rsplit("_", 1)

            if len(objs) == 1:
                pruned_tags.append(tag)
                continue

            color, obj = objs
            if color in COLORS:
                print("Removed: ", tag)
                continue

            else:
                print(f"New Color: {color}?")

            pruned_tags.append(tag)

        line = ", ".join(pruned_tags)

        with open(FILE, "w", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":

    args = params(1, 1, ("path to folder",))
    prune(*args)
