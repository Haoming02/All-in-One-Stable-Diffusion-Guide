from PIL import Image, UnidentifiedImageError
import os


def optimize(FOLDER: str):
    i = 0

    for FILE in os.listdir(FOLDER):
        OBJ = os.path.join(FOLDER, FILE)

        if os.path.isdir(OBJ):
            # optimize(OBJ)
            continue

        if not FILE.lower().endswith(".png"):
            continue

        try:
            img = Image.open(OBJ)
            w, h = img.size

            if abs(w - h) < 4:
                w = 1360
                h = 1360
            elif w > h:
                w = int(round(float(w / h) * 12.0) * 100)
                h = 1200
            else:
                h = int(round(float(h / w) * 12.0) * 100)
                w = 1200

            img = img.convert("RGB").resize((w, h), resample=Image.LANCZOS)
            img.save(
                os.path.join(FOLDER, f"{i:02d}.jpg"),
                optimize=True,
                quality=100,
            )

            i += 1

        except UnidentifiedImageError:
            continue


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print('\nUsage:\npython PrepJPG.py "<path to folder>"')
        raise SystemExit
    elif len(sys.argv) > 2:
        print('\nUse " " to encapsulate your path')
        raise SystemExit

    optimize(sys.argv[1])
