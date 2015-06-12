# Version Updater
This is a utility to update version in all necessary files. 

Sometimes there are too many files in the project which contains project version as hardcoded. For example you would be having files bower.json and setup.py on same version in your project. Whenever the version is wanted be to upgrade, all files were updated one by one. With this one, all implemented files can be update simply at once. It will find your version files and update them one by one.

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

## Built-In Files
* setup.py
* bower.json
* package.json

### ComingSoon
* pom.xml



## Implement Your Custom Files

Any file implementation can be added simply. `version-updater` reads extra config from `.vurc` file under your current directory or your user home directory. 

Here is a simple example of `.vurc`

```bash
$ vi ~/.vurc
```
or
```bash
$ vi /path/to/your_project/.vurc
```

```json
{
	files : [
		{
            'name': 'my_custom_file.txt',
            'regex': '(?P<match_left>version=")(?P<version>\d+)(?P<match_right>")'		
		}
	]
}
```

Any famous file formats can be demanded as built-in by opening an issue. Feel free to demand it.

