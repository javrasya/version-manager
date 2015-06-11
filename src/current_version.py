import glob
import os

from src.config import CONFIG
from src.strategies.file import file_strategy_registry


def main():
    for f in CONFIG.get("FILES"):
        cls = file_strategy_registry.get(f)
        for path in glob.glob(f):
            print "File %s version is %s" % (path, cls(os.path.abspath(path)).current_version)


if __name__ == '__main__':  # pragma: no cover
    main()
