from Formatter import params, listdir
from PIL import Image
import os


def optimize(folder: str, delete: str):
    delete: bool = delete is not None

    for file in listdir(folder, ".png"):
        img = Image.open(file)
        img.save(file.replace(".png", ".jpg"), optimize=True, quality=100)
        if delete:
            os.remove(file)


if __name__ == "__main__":
    args = params(1, 2, ("path to folder", "delete original"))
    optimize(*args)
