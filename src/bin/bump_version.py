import sys
import warnings
from src.bin.command import Command, get_valid_key
from src.file import loaded_files


class BumpVersion(Command):
    help_content = {
        '--major': 'To upgrade major version',
        '--minor': 'To upgrade minor version',
        '--patch': 'To upgrade patch version'
    }
    expected_args = ['--major', '--minor', '--patch']

    def __init__(self):
        super(BumpVersion, self).__init__()
        bumps = []
        for earg in self.expected_args:
            v = get_valid_key(earg)
            if getattr(self, v):
                bumps.append(v)
        if len(bumps) > 1:
            warnings.warn('Single bump is allowed at a time. Only %s will be applied' % bumps[0], Warning)

    def execute(self):
        if super(BumpVersion, self).execute():
            for file in loaded_files:
                file.bump_version(get_valid_key(self.args[0]))


if __name__ == '__main__':  # pragma: no cover
    BumpVersion().execute()
