from Formatter import params
from PIL.PngImagePlugin import PngInfo
from PIL import Image
import os


def copy_metadata(source: str, destination: str):
    assert os.path.isfile(source) and os.path.isfile(destination)
    assert source.endswith(".png") and destination.endswith(".png")

    source_image = Image.open(source)
    metadata = PngInfo()

    if "parameters" in source_image.info.keys():
        print("Detected Automatic1111")
        metadata.add_text("parameters", source_image.info["parameters"])

    elif "workflow" in source_image.info.keys():
        print("Detected ComfyUI")
        metadata.add_text("prompt", source_image.info["prompt"])
        metadata.add_text("workflow", source_image.info["workflow"])

    else:
        raise ValueError("No Metadata Detected...")

    destination_image = Image.open(destination)
    destination_image.save(destination, optimize=True, pnginfo=metadata)


if __name__ == "__main__":
    args = params(2, 2, ("path to source", "path to target"))
    copy_metadata(*args)
