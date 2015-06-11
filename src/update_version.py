import glob
import os
import sys
from src.config import CONFIG
from src.strategies.file import file_strategy_registry


def main():
    version = sys.argv[1]
    for f in CONFIG.get("FILES"):
        cls = file_strategy_registry.get(f)
        for path in glob.glob(f):
            cls(os.path.abspath(path)).update_version(version)


if __name__ == '__main__':  # pragma: no cover
    main()
