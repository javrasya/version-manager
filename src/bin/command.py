import sys

__author__ = 'ahmetdal'


class Command(object):
    base_help_content = {'--help': 'To get help about command'}
    base_expected_args = ['--help']

    help_content = {}
    expected_args = []
    expected_keys = []

    def __init__(self):
        self.base_help_content.update(self.help_content)
        self.base_expected_args += self.expected_args

        self.kwargs = dict(x.split('=', 1) for x in sys.argv[1:] if '=' in x)
        self.args = list(x for x in sys.argv[1:] if '=' not in x)

        for k, v in self.kwargs.items():
            if v not in self.expected_keys:
                raise Exception('%s is not valid key for command %s' % (k, self.__module__))

        for earg in self.base_expected_args:
            setattr(self, get_valid_key(earg), earg in self.args)

        for ekey in self.expected_keys:
            setattr(self, get_valid_key(ekey), self.kwargs.get(ekey, None))

    def promt_help(self):
        for k, v in self.base_help_content.items():
            print("%s -> %s" % (k, v))

    def execute(self):
        if self.help:
            self.promt_help()
            return False
        return True


def get_valid_key(key):
    return key.replace('-', '')
