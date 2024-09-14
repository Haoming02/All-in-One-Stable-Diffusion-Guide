from Formatter import params, listdir
from PIL import Image


def optimize(folder: str):

    for FILE in listdir(folder, ".png"):
        img = Image.open(FILE)
        img.save(FILE.replace(".png", ".jpg"), optimize=True, quality=100)


if __name__ == "__main__":

    args = params(1, 1, ("path to folder",))
    optimize(*args)
