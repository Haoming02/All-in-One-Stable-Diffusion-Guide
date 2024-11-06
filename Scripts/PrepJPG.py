from Formatter import params, listdir
from PIL import Image
import os

RATIOS: tuple[float] = (
    1.0,
    1.1333,
    1.2857,
    1.4615,
    1.6667,
    1.9091,
    2.2,
    2.5556,
    3.0,
)


def find_closest(og_w: int, og_h: int) -> tuple[int, int]:
    ratio: float = max(og_w, og_h) / min(og_w, og_h)
    for r in RATIOS:
        if r >= ratio:
            target = r
            break

    if og_w > og_h:
        w = og_w
        h = round(og_w / target)

    else:
        h = og_h
        w = round(og_h / target)

    return w, h


def safety_check(file: str) -> bool:
    filename, extension = os.path.splitext(os.path.basename(file))

    if extension == ".jpg" and filename.isdecimal():
        backup = file.replace(".jpg", ".bak")
        if os.path.exists(backup):
            os.remove(backup)
        os.rename(file, backup)
        return False

    return True


def load_image(path: str) -> Image.Image:
    img = Image.open(path)
    if img.mode != "RGB":
        bg = Image.new("RGBA", img.size, (127, 127, 127, 255))
        bg.paste(img, (0, 0), img)
        img = bg.convert("RGB")

    return img


def crop(img: Image.Image, new_w: int, new_h: int) -> Image.Image:
    w, h = img.size

    new_w = new_w - (new_w % 2)
    new_h = new_h - (new_h % 2)

    left = (w - new_w) // 2
    up = (h - new_h) // 2
    right = left + new_w
    bottom = up + new_h

    return img.crop((left, up, right, bottom))


def optimize(path: str, keep: bool):
    keep_filename: bool = keep is not None
    i = 0

    for file in listdir(path, (".jpg", ".jpeg", ".png", ".webp")):
        if (not keep_filename) and (not safety_check(file)):
            continue

        img = load_image(file)
        w, h = img.size

        if w != h:
            new_w, new_h = find_closest(w, h)
            img = crop(img, new_w, new_h)

        if keep_filename:
            name, ext = os.path.splitext(file)
            if ext in (".jpg", ".jpeg"):
                filename = file
            else:
                filename = f"{name}.jpg"

        else:
            folder: str = os.path.dirname(file)
            filename: str = os.path.join(folder, f"{i:02d}.jpg")
            i += 1

        qp: int = min(1.0, (2048 * 2048) / (new_w * new_h)) * 100
        img.save(filename, quality=int(qp), optimize=True)


if __name__ == "__main__":

    args = params(1, 2, ("path to folder", "keep filename"))
    optimize(*args)
