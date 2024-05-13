from Formatter import params
from PIL.PngImagePlugin import PngInfo
from PIL import Image


def copy_data(source_path: str, destination_path: str):
    assert source_path.endswith(".png") and destination_path.endswith(".png")

    source_image = Image.open(source_path)

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

    destination_image = Image.open(destination_path)
    destination_image.save(destination_path, pnginfo=metadata)


if __name__ == "__main__":
    import os

    source, target = params(
        2, 2, os.path.basename(__file__), ["path to source", "path to target"]
    )

    copy_data(source, target)
