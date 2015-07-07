from src.file import loaded_files
from colorama import Fore, Back, Style


def main():
    for file in loaded_files:
        print  "%sFile %s version is %s\n" % (file.color, file.path, file.current_version)


if __name__ == '__main__':  # pragma: no cover
    main()
