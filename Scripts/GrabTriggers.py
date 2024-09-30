from Formatter import format, params, listdir


def debug(FOLDER: str, from_idx: int, to_idx: int):
    from_idx, to_idx = int(from_idx), int(to_idx)

    files = list(listdir(FOLDER, ".txt"))
    triggers = set()

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            line = f.read()
        tags = format(line)

        triggers.add(", ".join(tags[from_idx:to_idx]))

    triggers = '", "'.join(list(triggers))
    print(f'"{triggers}"')


if __name__ == "__main__":

    args = params(3, 3, ("path to folder", "from", "to"))
    debug(*args)
