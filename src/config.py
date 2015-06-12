from copy import deepcopy
import json
from os.path import expanduser

__author__ = 'ahmetdal'

_RC_FILE = '.vurc'

_RC_LOOKUP_PATHS = [
    expanduser("~/"),
    './'
]

_INITIAL_CONFIG = {
    'files': [
        {
            'name': 'setup.py',
            'regex': '(?P<match_left>version\s*=\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
        },
        {
            'name': 'bower.json',
            'regex': '(?P<match_left>"version"\s*:\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
        },
        {
            'name': 'package.json',
            'regex': '(?P<match_left>"version"\s*:\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
        },
    ],
    'excludes': [
        '.git',
        '.tmp',
        'dist',
        'build',
        'node_modules',
        'bower_components',
        '.tox'
    ]
}


def load_config():
    """
    # This is default case which there is not .vurc file in user home and current directories.
    >>> config=load_config()
    >>> _INITIAL_CONFIG==config
    True


    # This is the case which the config is extended from .vurc file in current directory.
    >>> from shutil import copyfile
    >>> import os
    >>> from os.path import dirname
    >>> copyfile(os.path.join(dirname(dirname(__file__)),'test_resources','.vurc'),os.path.join(os.getcwd(),'.vurc'))
    >>> config=load_config()
    >>> expected_config=deepcopy(_INITIAL_CONFIG)
    >>> expected_config["files"].append({"name":"test_files"})
    >>> expected_config["excludes"].append("test_excludes")
    >>> config == expected_config
    True
    >>> os.remove(os.path.join(os.getcwd(),'.vurc'))
    """

    _LOADED_CONFIG = deepcopy(_INITIAL_CONFIG)
    for lookup_path in _RC_LOOKUP_PATHS:
        try:
            with open("%s%s" % (lookup_path, _RC_FILE)) as f:
                config = json.loads(f.read())
                _LOADED_CONFIG["files"].extend(config.get("files", []))
                _LOADED_CONFIG["excludes"].extend(config.get("excludes", []))
        except IOError as e:
            pass

    return _LOADED_CONFIG
