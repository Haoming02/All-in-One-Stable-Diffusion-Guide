from PIL.PngImagePlugin import PngInfo
from PIL import Image
import sys

def copy_data(source_path:str, destination_path:str):

    metadata = PngInfo()
    source_image = Image.open(source_path)

    metadata.add_text("prompt", source_image.info['prompt'])
    metadata.add_text("workflow", source_image.info['workflow'])

    destination_image = Image.open(destination_path)
    destination_image.save(destination_path, pnginfo=metadata)

if __name__ == '__main__':
    copy_data(sys.argv[1], sys.argv[2])
