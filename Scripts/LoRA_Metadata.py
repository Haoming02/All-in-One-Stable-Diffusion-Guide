from Formatter import params
from json import loads, dump
from struct import unpack


def read(path: str):
    assert path.endswith(".safetensors")

    with open(path, "rb") as mdl:
        length_of_header = unpack("<Q", mdl.read(8))[0]
        header_data = mdl.read(length_of_header)
        header = loads(header_data)
        config: dict = header.get("__metadata__", None)

    if not config:
        print("\nNo Metadata Detected!")
        raise SystemExit

    for key in ("ss_tag_frequency", "ss_bucket_info", "ss_dataset_dirs"):
        config.pop(key, None)

    preset: dict = {}

    for key in config.keys():
        preset[key.split("ss_", 1)[-1]] = config[key]

    with open(f"{path}.json", "w+", encoding="utf-8") as f:
        dump(dict(sorted(preset.items())), f)


if __name__ == "__main__":
    args = params(1, 1, ("path to safetensor",))
    read(*args)
