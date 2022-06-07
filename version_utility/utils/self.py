import toml


def readVersion(file: str = "pyproject.toml") -> str:
    with open(file, "r") as tomlFile:
        data: dict = toml.load(tomlFile)
        version: str = data["tool"]["poetry"]["version"]
        tomlFile.close()
    return version
