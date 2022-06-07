from argparse import Namespace
from pathlib import Path

import toml

from version_utility.utils.args import mainArgs


def readFile(file: str = "pyproject.toml") -> dict:
    path: Path = Path(file)
    extension: str = path.suffix

    with open(file, "r") as versionFile:
        match extension:
            case ".toml":
                data: dict = toml.load(versionFile)
                return data
        versionFile.close()


def readVersion(data: dict) -> str:
    return data["tool"]["poetry"]["version"]


def setVersion(version: str, file: str = "pyproject.toml") -> str:
    path: Path = Path(file)
    extension: str = path.suffix
    data: dict = readFile(file=file)

    data["tool"]["poetry"]["version"] = version
    with open(file, "w") as versionFile:
        match extension:
            case ".toml":
                data: dict = toml.dump(data, versionFile)
        versionFile.close()


def main() -> None:
    args: Namespace = mainArgs()

    if args.read_version:
        print(readVersion(file=args.file))

    elif args.set_version:
        setVersion(version=args.set_version, file=args.file)

    else:
        print("Invalid command line arguements")


if __name__ == "__main__":
    main()
