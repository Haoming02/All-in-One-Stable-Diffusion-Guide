from Formatter import params
from json import load, dump


def minify(path: str):
    assert path.endswith(".json")
    with open(path, "r", encoding="utf-8") as f:
        data = load(f)
    with open(path, "w", encoding="utf-8") as f:
        dump(data, f, separators=(",", ":"))


if __name__ == "__main__":

    args = params(1, 1, ("path to json",))
    minify(*args)
