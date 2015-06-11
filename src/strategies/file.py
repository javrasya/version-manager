import re
from src.registry import Registry

__author__ = 'ahmetdal'

file_strategy_registry = Registry()


class FileStrategyBase(type):
    def __new__(cls, *args, **kwargs):
        cls = type.__new__(cls, *args, **kwargs)
        if hasattr(cls, "name") and cls.name:
            file_strategy_registry.register(cls.name, cls)

        return cls


version_pattern = re.compile(r'((\d)+.?)+')


class FileStrategy:
    name = None
    regex = None
    __metaclass__ = FileStrategyBase

    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as f:
            self.file_content = f.read()

    @property
    def current_version(self):
        if self.regex:
            self.pattern = re.compile(self.regex)
            match = self.pattern.search(self.file_content)
            if match:
                return match.groups()[1]
            else:
                raise Exception("No version definition is found in file %s" % self.file_path)
        else:
            raise Exception("File release regex can not be None.")

    def __validate_version(self, version):
        return version_pattern.search(version) is not None

    def update_version(self, new_version):
        if not self.__validate_version(new_version):
            raise Exception("Invalid version %s. Version should be in a pattern like %s" % (new_version, version_pattern.pattern))

        print 'File %s is now on version %s' % (self.file_path, self.current_version)
        self.file_content = re.sub(
            self.pattern,
            lambda m:
            m.group('match_left') + new_version + m.group('match_right'),
            self.file_content,
            re.MULTILINE
        )
        with open(self.file_path, 'w') as f:
            f.write(self.file_content)
        print 'File %s is updated to version %s\n' % (self.file_path, self.current_version)

    def next_version(self):
        raise NotImplementedError()

    def previous_version(self):
        raise NotImplementedError()
