from src.file import loaded_files


def main():
    for file in loaded_files:
        print "File %s version is %s" % (file.path, file.current_version)


if __name__ == '__main__':  # pragma: no cover
    main()
