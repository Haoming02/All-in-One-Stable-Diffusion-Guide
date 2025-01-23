from Formatter import params, listdir
from PIL import Image
import os


def create(folder: str):
    for file in listdir(folder, (".jpg", ".jpeg", ".png", ".webp")):
        filename, ext = os.path.splitext(file)
        img = Image.open(file)
        img.transpose(Image.FLIP_LEFT_RIGHT).save(
            f"{filename}_h{ext}",
            optimize=True,
            quality=100,
        )

        if os.path.isfile(f"{filename}.txt"):
            with open(f"{filename}.txt", "r", encoding="utf-8") as f:
                caption = f.read()
            with open(f"{filename}_h.txt", "w+", encoding="utf-8") as f:
                f.write(caption)


if __name__ == "__main__":
    args = params(1, 1, ("path to folder",))
    create(*args)
