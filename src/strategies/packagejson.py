from src.strategies.file import FileStrategy

__author__ = 'ahmetdal'


class PackageJSONFileStrategy(FileStrategy):
    name = 'package.json'
    regex = '(?P<match_left>"version"\s*:\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
