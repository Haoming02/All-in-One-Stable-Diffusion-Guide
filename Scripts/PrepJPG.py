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


def find_closest(arr: float, value: float) -> float:
    closest = None
    for elem in arr:
        if elem > value:
            continue
        if closest is None or (value - elem) < (value - closest):
            closest = elem

    return closest


def safety_check(file: str) -> bool:
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


def optimize(FOLDER: str, target_width: int, target_height: int):
    RATIOS = init_ratios()

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

        w, h = img.size
        while w > 2048 or h > 2048:
            w //= 2
            h //= 2

        if (w, h) != img.size:
            img = img.resize((int(w), int(h)), Image.Resampling.LANCZOS)

        og_w, og_h = w, h

        if target_width and target_height:
            w = int(target_width)
            h = int(target_height)
            if w > og_w or h > og_h:
                w, h = og_w, og_h

        if w != h:
            ratio = w / h if w > h else h / w
            closest = find_closest(RATIOS, ratio)  # >= 1.0

            if w > h:
                w = int((h * closest) // 2 * 2)
                h = int(h // 2 * 2)
                dx = (og_w - w) // 2
                dy = (og_h - h) // 2

            else:
                h = int((w * closest) // 2 * 2)
                w = int(w // 2 * 2)
                dx = (og_w - w) // 2
                dy = (og_h - h) // 2

            img = img.crop((dx, dy, og_w - dx, og_h - dy))

        img.save(
            os.path.join(FOLDER, f"{i:02d}.jpg"),
            optimize=True,
            quality=100,
        )

        i += 1


if __name__ == "__main__":

    args = params(1, 3, ("path to folder", "width", "height"))
    optimize(*args)
