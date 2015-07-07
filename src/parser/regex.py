import re
from src.parser.parser import Parser

__author__ = 'ahmetdal'

REGEXP_PARSER = 'regexp'


class RegexParser(Parser):
    file_type = REGEXP_PARSER

    def __init__(self, regex=None, *args, **kwargs):
        super(RegexParser, self).__init__(*args, **kwargs)
        self.regex = regex
        if not self.regex:
            raise Exception("File version regex must be given for regex parser type.")
        self.pattern = re.compile(self.regex)

    def update_version(self, content, new_version):
        self.validate_version(new_version)
        content = re.sub(
            self.pattern,
            lambda m:
            m.group('match_left') + new_version + m.group('match_right'),
            content,
            re.MULTILINE
        )
        return content

    def current_version(self, content):
        match = self.pattern.search(content)
        if match:
            return match.group("version")
