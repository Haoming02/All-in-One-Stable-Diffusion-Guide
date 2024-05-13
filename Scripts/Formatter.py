def format(input_string: str) -> list[str]:
    """Split a string into a list of tags, while removing extra comma and space"""
    return list(filter(None, [word.strip() for word in input_string.split(",")]))


def params(min_arg: int, max_arg: int, filename: str, args: list[str]) -> list[str]:
    """Validate the number of passed-in arguments"""
    import sys

    parem: list = sys.argv[1:]

    if len(args) < min_arg or len(args) > max_arg:
        raise SystemError("\nInvalid Args Count")

    if len(parem) < min_arg:
        usage = '>" "<'.join(args)
        print(f'\nUsage:\npython {filename} "<{usage}>"')
        raise SystemExit

    if len(parem) > max_arg:
        print('\n[Error] Use " " to encapsulate your paths/tags!')
        raise SystemExit

    while len(parem) < max_arg:
        parem.append(None)

    return parem


def listdir(
    path: str, ext: str | list[str] = None, recursive: bool = None
) -> list[str]:
    """Return a list of all matching files"""
    import os

    path = path.strip()
    if not os.path.exists(path):
        print(f'\nPath "{path}" does not exist...')
        raise SystemExit

    FILES = []

    for f in os.listdir(path):
        obj = os.path.join(path, f)

        if os.path.isdir(obj):
            if recursive is None:
                i = input("\nRecursive [y/N]: ")
                recursive = i.strip() != "N"

            if recursive:
                FILES += listdir(obj, ext, True)

            continue

        if not ext:
            FILES.append(obj)

        elif type(ext) is str:
            if obj.endswith(ext):
                FILES.append(obj)

        else:
            for ex in ext:
                if obj.endswith(ex):
                    FILES.append(obj)

    return FILES


if __name__ == "__main__":

    (FOLDER,) = params(1, 1, "Formatter.py", ["path to folder"])
    files = listdir(FOLDER, ".txt")

    for file in files:

        with open(file, "r", encoding="utf-8") as f:
            original_line = f.read()

        tags = format(original_line)
        dedupe = []

        for tag in tags:
            if tag not in dedupe:
                dedupe.append(tag)

        line = ", ".join(dedupe)

        with open(file, "w", encoding="utf-8") as f:
            f.write(line)
