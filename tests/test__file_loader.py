import os
from shutil import copyfile
from unittest import TestCase
from os.path import dirname

from src.file import FileLoader
from src import config

__author__ = 'ahmetdal'


class test_FileLoader(TestCase):
    def setUp(self):
        config._INITIAL_CONFIG["groups"]["default"]['excludes'].append('setup.py')
        self.file_loader = FileLoader(["default"])
        try:
            os.remove(os.path.join(os.getcwd(), 'bower.json'))
        except OSError:
            pass

    def test_load_files_with_no_files(self):
        self.file_loader.load()
        self.assertEqual([], self.file_loader.loaded_files)

    def test_load_files(self):
        copyfile(os.path.join(dirname(dirname(__file__)), 'test_resources', 'test_file'), os.path.join(os.getcwd(), 'bower.json'))
        self.file_loader.load()
        self.assertEqual(1, len(self.file_loader.loaded_files))
        self.assertEqual('bower.json', self.file_loader.loaded_files[0].name)
        self.assertEqual('0.2.0', self.file_loader.loaded_files[0].current_version)
        os.remove(os.path.join(os.getcwd(), 'bower.json'))
