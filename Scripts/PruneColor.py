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
    "light aqua",
    "light black",
    "light blonde",
    "light blue",
    "light brown",
    "light cyan",
    "light light",
    "light green",
    "light grey",
    "light orange",
    "light pink",
    "light purple",
    "light lavender",
    "light red",
    "light silver",
    "light white",
    "light yellow",
    "light violet",
    # "multicolored",
    # "gradient",
    # "two-tone",
)

PRUNE: tuple[str] = ("hair between eyes",)
ALLOWED: tuple[str] = ("one eye closed", "closed eyes")


def prune(folder: str):
    DELETED = set()
    UNKNOWN = set()

    for file in listdir(folder, ".txt"):

        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        og_tags = format(line)
        pruned_tags = []

        for tag in og_tags:
            if tag in PRUNE:
                DELETED.add(tag)
                continue

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
                DELETED.add(tag)
                continue
            else:
                if not tag in ALLOWED:
                    UNKNOWN.add(tag)
                pruned_tags.append(tag)

        line = ", ".join(pruned_tags)

        with open(file, "w", encoding="utf-8") as f:
            f.write(line)

    print("\n[Removed]")
    print("\n".join(sorted(list(DELETED))))
    print("\n[Manual Check]")
    print("\n".join(sorted(list(UNKNOWN))))


if __name__ == "__main__":

    args = params(1, 1, ("path to folder",))
    prune(*args)
