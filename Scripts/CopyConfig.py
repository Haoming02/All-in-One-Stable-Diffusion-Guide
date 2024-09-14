from Formatter import params
from json import load, dump
import os


def copy_config(source: str, destination: str):
    assert source.endswith(".json") and destination.endswith(".json")
    assert os.path.isfile(source) and os.path.isfile(destination)

    with open(source, "r", encoding="utf-8") as f:
        old_config = load(f)

    with open(destination, "r", encoding="utf-8") as f:
        new_config = load(f)

    transfer_config = {k: old_config[k] for k in new_config if k in old_config}

    with open(destination, "w", encoding="utf-8") as f:
        dump(transfer_config, f)


if __name__ == "__main__":

    args = params(2, 2, ("path to source", "path to target"))
    copy_config(*args)
