from copy import deepcopy
from unittest import TestCase
from src.config import load_config, _INITIAL_CONFIG, _RC_FILE
from shutil import copyfile
import os
from os.path import dirname

__author__ = 'ahmetdal'


class test_Config(TestCase):
    def test_load_config(self):
        config = load_config(["default"])
        self.assertDictEqual({k: v for k, v in _INITIAL_CONFIG["groups"].items() if k is not "default_groups"}, config)

    def test_load_config_with_vmrc(self):
        # This is the case which the config is extended from .vmrc file in current directory.
        copyfile(os.path.join(dirname(dirname(__file__)), 'test_resources', _RC_FILE), os.path.join(os.getcwd(), _RC_FILE))
        config = load_config(["test"])
        expected_config = {
            "test":
                {
                    "files": [
                        {
                            "names": ["test_files"]
                        }
                    ],
                    "excludes": [
                        "test_excludes"
                    ]
                }
        }
        self.assertEqual(expected_config, config)
        os.remove(os.path.join(os.getcwd(), '.vmrc'))
