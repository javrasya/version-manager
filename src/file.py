import os
import re
from repoze.lru import CacheMaker
from src.config import load_config

cache_maker = CacheMaker()

__author__ = 'ahmetdal'

version_pattern = re.compile(r'((\d)+.?)+')


class File:
    """
    # current_version test
    >>> from os.path import dirname
    >>> file = File("test_file",os.path.join(dirname(dirname(__file__)),'test_resources','test_file'),'(?P<match_left>version\s*=\s*(?:"))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>")')
    >>> file.current_version
    '0.2.0'

    # update_version test
    >>> file.update_version('0.2.1')
    File /Users/ahmetdal/workspace/version-updater/test_resources/test_file is now on version 0.2.0
    File /Users/ahmetdal/workspace/version-updater/test_resources/test_file is updated to version 0.2.1
    <BLANKLINE>
    >>> file.current_version
    '0.2.1'
    >>> file.update_version('0.2.0')
    File /Users/ahmetdal/workspace/version-updater/test_resources/test_file is now on version 0.2.1
    File /Users/ahmetdal/workspace/version-updater/test_resources/test_file is updated to version 0.2.0
    <BLANKLINE>

    """

    def __init__(self, name, path, regex):
        self.name = name
        self.path = path
        self.regex = regex
        with open(self.path, 'r') as f:
            self.content = f.read()
        if self.regex:
            self.pattern = re.compile(self.regex)
        else:
            raise Exception("File release regex can not be None.")

    @property
    @cache_maker.lrucache(maxsize=300, name="current_version")
    def current_version(self):
        match = self.pattern.search(self.content)
        if match:
            return match.group('version')
        else:
            print "No version definition is found in file %s" % self.path

    def __validate_version(self, version):
        return version_pattern.search(version) is not None

    def update_version(self, new_version):
        if not self.__validate_version(new_version):
            raise Exception("Invalid version %s. Version should be in a pattern like %s" % (new_version, version_pattern.pattern))

        print 'File %s is now on version %s' % (self.path, self.current_version)
        self.content = re.sub(
            self.pattern,
            lambda m:
            m.group('match_left') + new_version + m.group('match_right'),
            self.content,
            re.MULTILINE
        )
        with open(self.path, 'w') as f:
            f.write(self.content)

        cache_maker.clear("current_version")
        print 'File %s is updated to version %s\n' % (self.path, self.current_version)

    def next_version(self):
        raise NotImplementedError()

    def previous_version(self):
        raise NotImplementedError()


loaded_files = []


class FileLoader:
    """
    >>> from shutil import copyfile
    >>> import os
    >>> from os.path import dirname

    >>> file_loader=FileLoader()
    >>> file_loader.load()
    >>> loaded_files
    []

    >>> copyfile(os.path.join(dirname(dirname(__file__)),'test_resources','test_file'),os.path.join(os.getcwd(),'setup.py'))
    >>> file_loader.load()
    >>> len(loaded_files)
    1
    >>> loaded_files[0].name
    'setup.py'
    >>> loaded_files[0].current_version
    '0.2.0'
    >>> os.remove(os.path.join(os.getcwd(),'setup.py'))
    """

    def __init__(self):
        self.config = load_config()
        self.files = self.config.get("files", [])
        self.excludes = self.config.get("excludes", [])

    def load(self):
        for dirpath, dirnames, files in os.walk('./'):
            for exclude in self.excludes:
                try:
                    dirnames.remove(exclude)
                except ValueError:
                    pass

            for f in files:
                config_files = filter(lambda x: x.get('name') == f, self.files)
                for config_file in config_files:
                    loaded_files.append(File(config_file.get('name'), os.path.abspath(os.path.join(dirpath, f)), config_file.get('regex', None)))


FileLoader().load()
