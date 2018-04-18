import argparse
import itertools
import os

from src.file import FileLoader
from src.helper import console


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--groups', help='To run specific group of files', default=None)
    parser.add_argument('--status', action='store_true', help='To see current status of versioning files')
    parser.add_argument('--set', help='To set specific version into version files. (--set 3.5.1)')
    parser.add_argument('--bump', choices=['major', 'minor', 'patch'],
                        help='To bump version defined as SemVer. Choices are ["major", "minor", "patch"] (--bump major)')

    args = parser.parse_args()
    groups = args.groups.split(",") if args.groups else None
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
    loaded_files = get_loader(groups).loaded_files
    for group, files in itertools.groupby(loaded_files, key=lambda f: f.group):
        console.print_data(
            ['File', 'Version', 'Path'],
            map(lambda f: [f.color + f.name, f.current_version, f.path.replace(os.getcwd(), ".").replace(f.name, "")], files),
            title=group
        )


def set(version, groups):
    loaded_files = get_loader(groups).loaded_files
    for group, files in itertools.groupby(loaded_files, key=lambda f: f.group):
        table_data = []
        for f in files:
            f.update_version(version)
            table_data.append([f.color + f.name, f.current_version, f.previous_version, f.path.replace(os.getcwd(), ".").replace(f.name, "")])
        console.print_data(
            ['File', 'New Version', 'Old Version', 'Path'],
            table_data,
            title=group
        )


def bump(level, groups):
    loaded_files = get_loader(groups).loaded_files
    for group, files in itertools.groupby(loaded_files, key=lambda f: f.group):
        table_data = []
        for f in files:
            f.bump_version(level)
            table_data.append([f.color + f.name, f.current_version, f.previous_version, f.path.replace(os.getcwd(), ".").replace(f.name, "")])
        console.print_data(
            ['File', 'New Version', 'Old Version', 'Path'],
            table_data,
            title=group
        )


if __name__ == '__main__':  # pragma: no cover
    main()
