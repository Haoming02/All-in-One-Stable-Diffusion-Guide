from Formatter import params, listdir
from PIL import Image
import os


def generate(folder: str):
    for file in listdir(folder, (".jpg", ".jpeg", ".png", ".webp")):

        if "masklabel" in file:
            continue

        filename = os.path.splitext(file)[0]
        mask = f"{filename}-masklabel.png"

        Image.open(file).convert("L").save(mask, optimize=True)


if __name__ == "__main__":

    args = params(1, 1, ("path to folder",))
    generate(*args)
