from Formatter import params, listdir


def filter_file(folder: str, filter: str):
    MATCH = set()

    for FILE in listdir(folder, ".txt"):

        with open(FILE, "r", encoding="utf-8") as f:
            line = f.read().strip()

        if filter in line:
            MATCH.add(FILE)

    print("\n".join(list(MATCH)))


if __name__ == "__main__":

    args = params(2, 2, ("path to folder", "tag"))
    filter_file(*args)
