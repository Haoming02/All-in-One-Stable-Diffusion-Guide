from Formatter import format, params, listdir
import os


def delete(path: str, filter: str):
    for file in listdir(path, ".txt"):

        with open(file, "r", encoding="utf-8") as f:
            line = f.read()

        og_tags = format(line)

        if filter in og_tags:
            os.remove(file)

            for fmt in (".png", ".jpg", ".jpeg", ".webp"):
                if os.path.isfile(file.replace(".txt", fmt)):
                    os.remove(file.replace(".txt", fmt))
                    break


if __name__ == "__main__":

    args = params(2, 2, ("path to folder", "tag"))
    delete(*args)
