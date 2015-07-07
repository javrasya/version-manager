# Version Manager 
[![Build Status](https://travis-ci.org/javrasya/version-manager.svg)](https://travis-ci.org/javrasya/version-updater) [![Coverage Status](https://coveralls.io/repos/github/javrasya/version-manager/badge.svg?branch=master)](https://coveralls.io/github/javrasya/version-updater?branch=master)

This is a utility to manage versions in all necessary files.(see,update, etc.) 

Sometimes there are too many files in the project which contains project version as hardcoded. For example you would be having files bower.json and setup.py on same version in your project. Whenever the version is wanted be to upgrade, all files were updated one by one. With this one, all implemented files can be update simply at once. It will find your version files and update them one by one.

This is installed into your python virtualenvironment and the commands below can be access from command-line directly.

## Installation
```bash
#Activate your virtuanenvironment and run this.
(sudo) pip install git+https://github.com/javrasya/version-manager.git
```


## Supported Functionalities
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
* pom.xml

### Print Color
* <span style="color:green;">setup.py - GREEN</span>
* <span style="color:red;">package.json - RED</span>
* <span style="color:yellow;background-color:grey">bower.json - YELLOW</span>
* <span style="color:magenta;">pom.xml - MAGENTA</span>


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

```javascript
{
	files : [
		{
            'name': 'my_custom_file.txt',
            'parser': 'regexp',
            'kwargs':{
            	'regex': '(?P<match_left>version=")(?P<version>\d+)(?P<match_right>")'
            }
		},
		{
            'name': 'my_custom_file.xml',
            'parser': 'xml',
            'kwargs':{
            	'xpaths': ['./ns:path1/ns:path2'],
            	'namespaces':{'':'my-name-space-uri'}
            }
		}		
	]
}
```

Any famous file formats can be demanded as built-in by opening an issue. Feel free to demand it.

