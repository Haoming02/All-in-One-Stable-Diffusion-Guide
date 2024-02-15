from PIL.PngImagePlugin import PngInfo
from PIL import Image

def copy_data(source_path:str, destination_path:str):
    assert source_path.endswith('.png') and destination_path.endswith('.png')

    source_image = Image.open(source_path)

    metadata = PngInfo()
    metadata.add_text("prompt", source_image.info['prompt'])
    metadata.add_text("workflow", source_image.info['workflow'])

    destination_image = Image.open(destination_path)
    destination_image.save(destination_path, pnginfo=metadata)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('\nUsage:\npython CopyMetadata.py "<path to source>" "<path to target>"')
        raise SystemExit
    elif len(sys.argv) > 3:
        print('\nUse " " to encapsulate your paths')
        raise SystemExit

    copy_data(sys.argv[1], sys.argv[2])
