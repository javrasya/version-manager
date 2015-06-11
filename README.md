# Version Updater
This is a utility to update version in all necessary files. 

Sometimes there are too many files in the project which contains project version as hardcoded. For example you would be having files bower.json and setup.py on same version in your project. Whenever the version is wanted to upgrade, all files were updated one by one. With this one, all implemented files can be update at once simply. 

This is installed into your python virtualenvironment and the commands below can be access from command-line directly.

## Installation
```bash
#Activate your virtuanenvironment and run this.
pip install git+https://github.com/javrasya/version-updater.git
```


## Supported Functionality
### See Current Version
To see current version of files.
```bash
$ current_version
```

#### Update version
Any version can be set.
```bash
$ update_version 1.1.1
```

#### Next Version(Cooming Soon)
Simply upgrade to next version.
```bash
$ next_version
```

#### Previous Version(Cooming Soon)
Simply downgrade to previous version.
```bash
$ previous_version
```

## Supported Files
* setup.py
* bower.json
* package.json

### ComingSoon
* pom.xml

