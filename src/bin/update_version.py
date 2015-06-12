import sys
from src.file import loaded_files


def main():
    version = sys.argv[1]
    for file in loaded_files:
        file.update_version(version)


if __name__ == '__main__':  # pragma: no cover
    main()
