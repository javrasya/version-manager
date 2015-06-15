import os
from unittest import TestCase
from os.path import dirname
from src.file import File

__author__ = 'ahmetdal'


class test_File(TestCase):
    def setUp(self):
        self.file = File("test_file", os.path.join(dirname(dirname(__file__)), 'test_resources', 'test_file'), '(?P<match_left>"version"\s*:\s*(?:"))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>")')
        self.file.update_version('0.2.0')

    def test_current_version(self):
        # current_version test
        self.assertEquals('0.2.0', self.file.current_version)

    def test_update_version(self):
        # update_version test

        self.file.update_version('0.2.1')
        self.assertEqual('0.2.1', self.file.current_version)
        self.file.update_version('0.2.0')
