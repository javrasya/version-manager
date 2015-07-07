import re

__author__ = 'ahmetdal'

PARSER_REGISTRY = {}


class ParserBase(type):
    def __new__(cls, *args, **kwargs):
        result = super(ParserBase, cls).__new__(cls, *args, **kwargs)
        if hasattr(result, 'file_type') and result.file_type:
            PARSER_REGISTRY[result.file_type] = result

        return result


version_pattern = re.compile(r'((\d)+.?)+')


class Parser():
    file_type = None
    __metaclass__ = ParserBase

    def current_version(self, content):
        raise NotImplementedError()

    def update_version(self, content, new_version):
        raise NotImplementedError()

    def next_version(self):
        raise NotImplementedError()

    def previous_version(self):
        raise NotImplementedError()

    @classmethod
    def validate_version(cls, version):
        if not version_pattern.search(version):
            raise Exception("Invalid version %s. Version should be in a pattern like %s" % (version, version_pattern.pattern))
