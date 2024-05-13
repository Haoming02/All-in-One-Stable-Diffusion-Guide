from Formatter import params, listdir
from PIL import Image


def optimize(FOLDER: str):
    files = listdir(FOLDER, ".png")

    for FILE in files:
        img = Image.open(FILE).convert("RGB")
        img.save(FILE.replace(".png", ".jpg"), optimize=True, quality=100)


if __name__ == "__main__":
    import os

    (folder,) = params(1, 1, os.path.basename(__file__), ["path to folder"])

    optimize(folder)
