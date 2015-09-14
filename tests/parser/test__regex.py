import os
from unittest import TestCase
from os.path import dirname
from src.parser import RegexParser

__author__ = 'ahmetdal'


class testRegexParser(TestCase):
    def setUp(self):
        with open(os.path.join(dirname(dirname(dirname(__file__))), 'test_resources', 'test_file')) as f:
            self.content = f.read()
        self.parser = RegexParser(regex='(?P<match_left>"version"\s*:\s*(?:"))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>")')

    def test_regex_is_none(self):
        try:
            RegexParser()
            self.assertFalse(True)
        except Exception as e:
            self.assertEqual("File version regex must be given for regex parser type.", str(e))

    def test_current_version(self):
        # current_version test
        self.assertEquals('0.2.0', self.parser.current_version(self.content))

    def test_update_version(self):
        # update_version test
        content = self.parser.update_version(self.content, '0.2.1')
        updated_current_version = self.parser.current_version(content)
        self.assertEqual('0.2.1', updated_current_version)

    def test_update_with_invalid_version(self):
        try:
            self.parser.update_version(self.content, 'a.b.c')
            self.assertFalse(True)
        except Exception as e:
            self.assertTrue("Invalid version" in str(e))
