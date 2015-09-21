import sys
from src.bin.command import Command
from src.file import loaded_files


def main():
    version = sys.argv[1]
    for file in loaded_files:
        file.update_version(version)


class SetVersion(Command):
    def execute(self):
        if super(SetVersion, self).execute():
            for file in loaded_files:
                file.update_version(self.args[0])


if __name__ == '__main__':  # pragma: no cover
    main()
