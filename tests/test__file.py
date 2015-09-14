import os
from unittest import TestCase
from os.path import dirname

import sys
from colorama import Fore

from src.file import File
from src.parser import RegexParser

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

__author__ = 'ahmetdal'


class test_File(TestCase):
    def setUp(self):
        parser = RegexParser(regex='(?P<match_left>"version"\s*:\s*(?:"))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>")')
        self.file = File("test_file", os.path.join(dirname(dirname(__file__)), 'test_resources', 'test_file'), parser)
        self.file.update_version('0.2.0')

    def test_parser_none(self):
        try:
            File("test_file", os.path.join(dirname(dirname(__file__)), 'test_resources', 'test_file'), None)
            self.assertFalse(True)
        except Exception as e:
            self.assertEqual("Parser must be given.", str(e))

    def test_no_version_definition_is_found(self):
        out = StringIO()
        sys.stdout = out
        path = os.path.join(dirname(dirname(__file__)), 'test_resources', 'test_file')
        parser = RegexParser(regex='(?P<match_left>"version"\s*=\s*(?:"))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>")')
        self.file = File("test_file", path, parser)
        self.assertIsNone(self.file.current_version)
        self.assertEqual("%sNo version definition is found in file %s" % (Fore.WHITE, path), out.getvalue().strip())

    def test_current_version(self):
        # current_version test
        self.assertEquals('0.2.0', self.file.current_version)

    def test_update_version(self):
        # update_version test

        self.file.update_version('0.2.1')
        self.assertEqual('0.2.1', self.file.current_version)
        self.file.update_version('0.2.0')

    def test_update_with_invalid_version(self):
        try:
            self.file.update_version('a.b.c')
            self.assertFalse(True)
        except Exception as e:
            self.assertTrue("Invalid version" in str(e))
        self.assertEqual('0.2.0', self.file.current_version)

    def test_next_version(self):
        try:
            self.file.next_version()
            self.assertFalse(True)
        except NotImplementedError:
            pass

    def test_previous_version(self):
        try:
            self.file.previous_version()
            self.assertFalse(True)
        except NotImplementedError:
            pass
