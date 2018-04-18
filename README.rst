.. |Built Status| image:: https://travis-ci.org/javrasya/version-manager.svg
   :target: https://travis-ci.org/javrasya/version-manager

.. |Coverage Status| image:: https://coveralls.io/repos/github/javrasya/version-manager/badge.svg?branch=master
   :target: https://coveralls.io/github/javrasya/version-manager?branch=master

.. |Current Status GIF|  image:: https://user-images.githubusercontent.com/1279644/38930120-0fb9d5c0-430f-11e8-9f1d-918444af2cdc.gif

.. |Set Version GIF|  image:: https://user-images.githubusercontent.com/1279644/38930124-10243276-430f-11e8-8b5d-dd881e479a9f.gif

.. |Bump Patch Version GIF|  image:: https://user-images.githubusercontent.com/1279644/38930121-0fd405b2-430f-11e8-8d90-33a197f78d82.gif

.. |Bump Minor Version GIF|  image:: https://user-images.githubusercontent.com/1279644/38930122-0fef8490-430f-11e8-9e8a-8aafe6d8b178.gif

.. |Bump Major Version GIF|  image:: https://user-images.githubusercontent.com/1279644/38930123-1009614e-430f-11e8-97bf-ffb91c06fb92.gif


***************
Version Manager
***************

|Built Status| |Coverage Status|

This is a utility to manage versions in all necessary files in one place.(see,update, etc.) 

Sometimes there are too many files in the project which contains project version. For example you would be having files such as bower.json and setup.py on same version in your project. Whenever the version is wanted be to upgraded, all files were updated one by one; now all implemented files can be update simply at once. It will find your versioning files and update them one by one.

This is installed into your python environment and the commands below can be access from command-line directly.

Requirements
============
* ``Python 2.7`` or ``pypy2``


Installation
============

.. code-block:: bash

    $ (sudo) pip install version-manager --upgrade


Supported Functionalities
=========================
Current Status
--------------

To see current version of files.

.. code-block:: bash

    $ versionmanager --status

|Current Status GIF|

Set version
-----------

Any version can be set.

.. code-block:: bash

    $ versionmanager --set 1.1.1

|Set Version GIF|

Bump Version
------------

This is new functionality to upgrade version without knowing whole version string. It simply upgrade version as major, minor or patch as it is defined in SemVer.

.. code-block:: bash

    $ versionmanager --bump major

.. code-block:: bash

    $ versionmanager --bump minor

.. code-block:: bash

    $ versionmanager --bump patch

|Bump Patch Version GIF|
|Bump Minor Version GIF|
|Bump Major Version GIF|

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
* conf.py (version) (sphinx) - BLUE
* conf.py (release) (sphinx) - BLUE
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
     "default_groups" :[
         "staging"
     ],
     "groups": {
       "eu_prod": {
         "files": [
           {
             "names": [
               "*-prod-eu.properties"
             ],
             "parser": "regexp",
             "color": "yellow",
             "kwargs": {
               "regex": "(?P<match_left>my_version=)(?P<version>\\d+\\.\\d+\\.\\d+)(?P<match_right>\\n)"
             }
           },
           {
             "names": [
               "*-prod-eu-1.sql",
               "*-prod-eu-2.sql"
             ],
             "version_separator": "x",
             "parser": "regexp",
             "color": "lightyellow_ex",
             "kwargs": {
               "regex": "(?P<match_left>dependent_silo_eu_v)(?P<version>\\d+x\\d+x\\d+)(?P<match_right>_HIVE)"
             }
           }
         ]
       },
       "us_prod": {
         "files": [
           {
             "names": [
               "*-prod-eu.properties"
             ],
             "parser": "regexp",
             "color": "yellow",
             "kwargs": {
               "regex": "(?P<match_left>my_version=)(?P<version>\\d+\\.\\d+\\.\\d+)(?P<match_right>\\n)"
             }
           },
           {
             "names": [
               "*-prod-us-1.sql",
               "*-prod-us-2.sql",
               "*-prod-us-3.sql"
             ],
             "version_separator": "x",
             "parser": "regexp",
             "color": "lightyellow_ex",
             "kwargs": {
               "regex": "(?P<match_left>dependent_silo_us_v)(?P<version>\\d+x\\d+x\\d+)(?P<match_right>_HIVE)"
             }
           }
         ]
       },
       "staging": {
         "files": [
           {
             "names": [
               "*-staging-*.properties"
             ],
             "parser": "regexp",
             "color": "yellow",
             "kwargs": {
               "regex": "(?P<match_left>my_version=)(?P<version>\\d+\\.\\d+\\.\\d+)(?P<match_right>\\n)"
             }
           },
           {
             "names": [
               "*-staging-*-1.sql",
               "*-staging-*-2.sql"
             ],
             "version_separator": "x",
             "parser": "regexp",
             "color": "lightyellow_ex",
             "kwargs": {
               "regex": "(?P<match_left>dependent_silo_staging_v)(?P<version>\\d+x\\d+x\\d+)(?P<match_right>_HIVE)"
             }
           }
         ]
       }
     }
   }


Any famous file formats can be demanded as built-in by opening an issue. Feel free to demand it :-)

To run a command for specific group;

.. code-block:: bash

    $ # To check files specific to eu_prod and staging
    $ versionmanager --groups eu_prod,staging --status

    $ # To check files specific to all prod environments
    $ versionmanager --groups "*_prod" --status



Change Logs
===========

0.8.5(Stable)
-------------

* **Improvement** - Support overriding default groups in `.vmrc`

0.8.4
-----

* **Improvement** - Print outputs in tabular format
* **Improvement** - Support giving the group which is demanded to be used. Multiple group names can be given. Wildcard is also supported
* **Improvement** - Support being able to define different groups for custom version files
* **Improvement** - Support wildcard for file names in `.vmrc`
* **Improvement** - Support defining multiple file names for single regex in `.vmrc`


0.6.0
-----

* **Improvement** - ``current_version`` and ``update_version`` are merged as subcomment under ``versionmanager`` consolescript. ``versionmanager --status``, ``versionmanager --set <version>`` and ``versionmanager --bump <level>`` are available instead of ``current_version`` and ``update_version <version>`` .
* **Improvement** - SemVer support is added for bump versioning. ``versionmanager --bump <level>`` which level is one among (``major``,``minor``,``patch``)

  
0.5.1
-----

* **Improvement** - ``pypy`` support is added.
* **Bug** - When there is multiple regex config for same file, one of them was being applied. It is fixed. (version and relase in Sphinx conf.py)


0.5.0
-----

* **Improvement** - ``Sphinx`` ``conf.py`` support is added.
* **Improvement** - README file is in rst format now.

