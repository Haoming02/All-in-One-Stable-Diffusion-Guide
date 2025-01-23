from Formatter import format, params, listdir


def debug(folder: str, from_idx: str, to_idx: str):
    from_idx, to_idx = int(from_idx), int(to_idx)
    triggers = set()

    for file in listdir(folder, ".txt"):
        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        tags = format(line)
        triggers.add(", ".join(tags[from_idx:to_idx]))

    triggers = '", "'.join(list(triggers))
    print(f'"{triggers}"')


if __name__ == "__main__":
    args = params(3, 3, ("path to folder", "from", "to"))
    debug(*args)
