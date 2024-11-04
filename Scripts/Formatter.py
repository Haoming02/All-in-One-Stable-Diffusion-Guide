from typing import Generator


def format(string: str) -> list[str]:
    """Split a string into a list of tags, while removing extra commas and spaces"""
    return list(filter(None, [tag.strip() for tag in string.split(",")]))


def params(min_arg: int, max_arg: int, args: tuple[str]) -> list[str]:
    """Validate and return correct the number of arguments"""
    import sys

    parem: list[str] = sys.argv[1:]
    param_count: int = len(parem)

    assert min_arg <= len(args) <= max_arg

    if param_count < min_arg:
        usage = '>" "<'.join(args)
        import inspect
        import os

        filename = os.path.basename(inspect.stack()[1].filename)
        print(f'\n[Usage]\npython {filename} "<{usage}>"\n')
        raise SystemExit

    if param_count > max_arg:
        print('\n[Error] Use " " to encapsulate your paths/tags!\n')
        raise SystemExit

    return parem + [None] * (max_arg - param_count)


def listdir(
    path: str, ext: None | str | list[str] = None, recursive: None | bool = None
) -> Generator[str, None, None]:
    """Return a generator of all files with matching extension(s)"""
    import os

    path = path.strip().strip('"')
    if not os.path.isdir(path):
        print(f'\n[Error] Path "{path}" is not a folder...\n')
        raise SystemExit

    objs = [os.path.join(path, file) for file in os.listdir(path)]
    for obj in objs:

        if os.path.isdir(obj):
            if recursive is None:
                i = input("\nRecursive [y/N]: ")
                recursive = i.strip() != "N"
            if recursive:
                yield from listdir(obj, ext, True)
            continue

        if ext is None:
            yield obj
            continue
        else:
            ext = [ext] if isinstance(ext, str) else ext
            for ex in ext:
                if obj.endswith(ex):
                    yield obj
                    break


if __name__ == "__main__":

    (folder,) = params(1, 1, ("path to folder",))

    for file in listdir(folder, ".txt"):

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
