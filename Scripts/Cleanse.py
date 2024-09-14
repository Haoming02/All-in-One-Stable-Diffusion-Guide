from Formatter import params, listdir


def cleanse(folder: str):

    for FILE in listdir(folder, ".txt"):

        with open(FILE, "w", encoding="utf-8") as f:
            f.write("")


if __name__ == "__main__":
    
    args = params(1, 1, ("path to folder",))
    cleanse(*args)
