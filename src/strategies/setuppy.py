from src.strategies.file import FileStrategy

__author__ = 'ahmetdal'


class SetupPYFileStrategy(FileStrategy):
    name = 'setup.py'
    regex = '(?P<match_left>version\s*=\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
