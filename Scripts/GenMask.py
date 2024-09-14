from Formatter import params, listdir
from PIL import Image
import os


def generate(folder: str):

    for FILE in listdir(folder, [".jpg", ".jpeg", ".png"]):

        if "masklabel" in FILE:
            continue

        filename = os.path.splitext(FILE)[0]
        mask = f"{filename}-masklabel.png"

        Image.open(FILE).convert("L").save(mask)


if __name__ == "__main__":

    args = params(1, 1, ("path to folder",))
    generate(*args)
