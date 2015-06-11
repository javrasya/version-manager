from src.strategies.file import FileStrategy

__author__ = 'ahmetdal'


class BowerJSONFileStrategy(FileStrategy):
    name = 'bower.json'
    regex = '(?P<match_left>"version"\s*:\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
