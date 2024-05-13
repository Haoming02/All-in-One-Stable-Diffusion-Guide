from Formatter import params
import json


def copy_data(source_path: str, destination_path: str):
    assert source_path.endswith(".json") and destination_path.endswith(".json")

    with open(source_path, "r", encoding="utf-8") as f:
        old_config = json.load(f)

    with open(destination_path, "r", encoding="utf-8") as f:
        new_config = json.load(f)

    for K in new_config.keys():
        if K in old_config.keys():
            new_config[K] = old_config[K]

    with open(destination_path, "w", encoding="utf-8") as f:
        json.dump(new_config, f)


if __name__ == "__main__":
    import os

    source, target = params(
        2, 2, os.path.basename(__file__), ["path to source", "path to target"]
    )

    copy_data(source, target)
