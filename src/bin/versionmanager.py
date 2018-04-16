import argparse

from src.file import FileLoader


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--groups', help='To run specific group of files', default="default")
    parser.add_argument('--status', action='store_true', help='To see current status of versioning files')
    parser.add_argument('--set', help='To set specific version into version files. (--set 3.5.1)')
    parser.add_argument('--bump', choices=['major', 'minor', 'patch'],
                        help='To bump version defined as SemVer. Choices are ["major", "minor", "patch"] (--bump major)')

    args = parser.parse_args()
    groups = args.groups.split(",")
    if args.status:
        status(groups)
    elif args.set:
        set(args.set, groups)
    elif args.bump:
        bump(args.bump, groups)


def get_loader(groups):
    file_loader = FileLoader(groups)
    file_loader.load()
    return file_loader


def status(groups):
    for file in get_loader(groups).loaded_files:
        print("%sFile %s version is %s\n" % (file.color, file.path, file.current_version))


def set(version, groups):
    for file in get_loader(groups).loaded_files:
        file.update_version(version)


def bump(level, groups):
    for file in get_loader(groups).loaded_files:
        file.bump_version(level)


if __name__ == '__main__':  # pragma: no cover
    main()
