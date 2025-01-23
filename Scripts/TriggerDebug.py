from Formatter import format, params, listdir


def debug(folder: str, index: str, unique: str):
    index = int(index)
    unique: bool = unique is not None
    print("")

    if unique:
        triggers: dict[str, int] = {}
        for file in listdir(folder, ".txt"):
            with open(file, "r", encoding="utf-8") as f:
                line = f.read()

            tag = format(line)[index]
            triggers[tag] = triggers.get(tag, 0) + 1

        triggers = dict(
            sorted(
                triggers.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )

        max_width = max(len(tag) for tag in triggers.keys()) + 1
        for tag, count in triggers.items():
            print(f"{tag:<{max_width}} - {count}")

    else:
        files = list(listdir(folder, ".txt"))
        max_width = max(len(filename) for filename in files) + 1

        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                line = f.read()

            tags = format(line)
            print(f"{file:<{max_width}} {tags[index]}")


if __name__ == "__main__":
    args = params(2, 3, ("path to folder", "index", "unique"))
    debug(*args)
