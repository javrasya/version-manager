from copy import deepcopy
import json
from fnmatch import fnmatch
from os.path import expanduser
from colorama import Fore

__author__ = 'ahmetdal'

_RC_FILE = '.vmrc'

_RC_LOOKUP_PATHS = [
    expanduser("~/"),
    './'
]

_INITIAL_CONFIG = {
    'groups': {
        'default': {

            'files': [
                {
                    'names': ['setup.py'],
                    'color': "GREEN",
                    'parser': 'regexp',
                    'kwargs': {
                        'regex': '(?P<match_left>version\s*=\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
                    }

                },
                {
                    'names': ['conf.py'],
                    'color': "BLUE",
                    'parser': 'regexp',
                    'kwargs': {
                        'regex': '(?P<match_left>version\s*=\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
                    }

                },
                {
                    'names': ['conf.py'],
                    'color': "BLUE",
                    'parser': 'regexp',
                    'kwargs': {
                        'regex': '(?P<match_left>release\s*=\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
                    }

                },
                {
                    'names': ['bower.json'],
                    'color': "YELLOW",
                    'parser': 'regexp',
                    'kwargs': {
                        'regex': '(?P<match_left>"version"\s*:\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
                    }
                },
                {
                    'names': ['package.json'],
                    'color': "RED",
                    'parser': 'regexp',
                    'kwargs': {
                        'regex': '(?P<match_left>"version"\s*:\s*(?:"|\'))(?P<version>(?:(?:\d+)+.?)+)(?P<match_right>"|\')'
                    }
                },
                {
                    'names': ['pom.xml'],
                    'color': "MAGENTA",
                    'parser': 'xml',
                    'kwargs': {
                        'xpaths': ['./mvn:version', './mvn:parent/mvn:version'],
                        'namespaces': {'mvn': 'http://maven.apache.org/POM/4.0.0'}
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
    }
}


def load_config(groups):
    _LOADED_CONFIG = deepcopy(_INITIAL_CONFIG)
    for lookup_path in _RC_LOOKUP_PATHS:
        try:
            with open("%s%s" % (lookup_path, _RC_FILE)) as f:
                config = json.loads(f.read())
                _LOADED_CONFIG["groups"].update(config.get("groups", {}))
        except IOError as e:
            pass

    return {k: v for k, v in _LOADED_CONFIG["groups"].items() if any(map(lambda g: fnmatch(k, g), groups))}
