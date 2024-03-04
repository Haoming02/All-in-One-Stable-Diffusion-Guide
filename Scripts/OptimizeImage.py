from PIL import Image, UnidentifiedImageError
import os

def optimize(FOLDER: str, qp: int = 85, force_rgb: bool = False):
    for FILE in os.listdir(FOLDER):
        if os.path.isdir(os.path.join(FOLDER, FILE)):
            continue

        try:
            img = Image.open(os.path.join(FOLDER, FILE))
            if force_rgb:
                img = img.convert("RGB")
            img.save(os.path.join(FOLDER, FILE), optimize=True, quality=qp)

        except UnidentifiedImageError:
            continue


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print('\nUsage:\npython OptimizeImage.py "<path to folder>"')
        raise SystemExit
    elif len(sys.argv) > 2:
        print('\nUse " " to encapsulate your path')
        raise SystemExit

    optimize(sys.argv[1])
