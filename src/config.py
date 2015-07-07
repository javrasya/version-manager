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
            'parser': 'regexp',
            'kwargs': {
                'regex': '(?P<match_left>version\s*=\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
            }

        },
        {
            'name': 'bower.json',
            'parser': 'regexp',
            'kwargs': {
                'regex': '(?P<match_left>"version"\s*:\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
            }
        },
        {
            'name': 'package.json',
            'parser': 'regexp',
            'kwargs': {
                'regex': '(?P<match_left>"version"\s*:\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
            }
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
