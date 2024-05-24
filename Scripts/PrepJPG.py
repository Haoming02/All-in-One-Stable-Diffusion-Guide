from Formatter import params, listdir
from PIL import Image
import os


def init_ratios() -> list[float]:
    ratios = []

    w = 1024
    h = 1024

    for _ in range(9):
        ratios.append(w / h)
        w += 64
        h -= 64

    return ratios


def safety_check(file: str):
    filename, extension = os.path.splitext(os.path.basename(file))

    if extension == ".jpg":
        try:
            _ = int(filename)
            backup = file.replace(".jpg", ".bak")
            if os.path.exists(backup):
                os.remove(backup)
            os.rename(file, backup)
            return False

        except ValueError:
            pass

    return True


def optimize(FOLDER: str):
    RATIOs = init_ratios()

    files = listdir(FOLDER, [".jpg", ".jpeg", ".png"])
    i = 0

    for FILE in files:
        if not safety_check(FILE):
            continue

        img = Image.open(FILE)

        if img.mode != "RGB":
            bg = Image.new("RGBA", img.size, (127, 127, 127, 255))
            bg.paste(img, (0, 0), img)
            img = bg.convert("RGB")

        og_w, og_h = w, h = img.size

        if w != h:
            ratio = w / h if (w > h) else h / w
            closest = min(RATIOs, key=lambda x: abs(x - ratio))

            if w > h:
                w = int((og_h * closest) // 2 * 2)
                h = int(og_h // 2 * 2)
                dx = abs(og_w - w) // 2
                dy = 0

            else:
                h = int((og_w * closest) // 2 * 2)
                w = int(og_w // 2 * 2)
                dx = 0
                dy = abs(og_h - h) // 2

            img = img.crop((dx, dy, og_w - dx, og_h - dy))

        img.save(
            os.path.join(FOLDER, f"{i:02d}.jpg"),
            optimize=True,
            quality=100,
        )

        i += 1


if __name__ == "__main__":

    (folder,) = params(1, 1, os.path.basename(__file__), ["path to folder"])

    optimize(folder)
