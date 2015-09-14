.. |Built Status| image:: https://travis-ci.org/javrasya/version-manager.svg
   :target: https://travis-ci.org/javrasya/version-manager

.. |Coverage Status| image:: https://coveralls.io/repos/github/javrasya/version-manager/badge.svg?branch=master
   :target: https://coveralls.io/github/javrasya/version-manager?branch=master


***************
Version Manager
***************

|Built Status| |Coverage Status|

This is a utility to manage versions in all necessary files in one place.(see,update, etc.) 

Sometimes there are too many files in the project which contains project version. For example you would be having files such as bower.json and setup.py on same version in your project. Whenever the version is wanted be to upgraded, all files were updated one by one; now all implemented files can be update simply at once. It will find your versioning files and update them one by one.

This is installed into your python environment and the commands below can be access from command-line directly.

Installation
============

.. code-block:: bash

    $ (sudo) pip install version-manager


Supported Functionalities
=========================
See current version
-------------------
To see current version of files.

.. code-block:: bash

    $ current_version


Update version
--------------
Any version can be set.

.. code-block:: bash

    $ update_version 1.1.1

Next Version(Cooming Soon)
--------------------------
Simply upgrade to next version.

.. code-block:: bash

    $ next_version

Previous Version(Cooming Soon)
------------------------------
Simply downgrade to previous version.

.. code-block:: bash

    $ previous_version


Built-In Supported Files
========================

* setup.py
* bower.json
* package.json
* pom.xml
* conf.py (sphinx documentation config)

Print Color
-----------

* setup.py - GREEN
* conf.py (version) - BLUE
* conf.py (release) - BLUE
* package.json - RED
* bower.json - YELLOW
* pom.xml - MAGENTA


Implement for Your Custom Files
===============================

Any file implementation can be added simply. ``version-manager`` reads extra config from ``.vmrc`` file under your current directory(project folder maybe) or your user home directory. 

Here is a simple example of ``.vmrc``

.. code-block:: bash

    $ vi ~/.vmrc

or

.. code-block:: bash

    $ vi /path/to/your_project/.vmrc


.. code-block:: json

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
                              'xpaths': ['./ns:path1/ns:version'],
                              'namespaces':{'my_namespace':'my-name-space-uri'}
                        }
                  }           
            ]
    }


Any famous file formats can be demanded as built-in by opening an issue. Feel free to demand it :-)

