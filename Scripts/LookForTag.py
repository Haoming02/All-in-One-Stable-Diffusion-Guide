from Formatter import params, listdir


def filter_file(folder: str, filter: str):
    matches = set()

    for file in listdir(folder, ".txt"):
        with open(file, "r", encoding="utf-8") as f:
            line = f.read().strip()

        if filter in line:
            matches.add(file)

    print("\n".join(list(matches)))


if __name__ == "__main__":
    args = params(2, 2, ("path to folder", "tag"))
    filter_file(*args)
