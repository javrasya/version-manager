.. |Built Status| image:: https://travis-ci.org/javrasya/version-manager.svg
   :target: https://travis-ci.org/javrasya/version-manager

.. |Coverage Status| image:: https://coveralls.io/repos/github/javrasya/version-manager/badge.svg?branch=master
   :target: https://coveralls.io/github/javrasya/version-manager?branch=master

.. |Current Status GIF|  image:: https://cloud.githubusercontent.com/assets/1279644/10024585/9cd838f4-6160-11e5-9ef6-e53fb93e420c.gif

.. |Set Version GIF|  image:: https://cloud.githubusercontent.com/assets/1279644/10024586/9cdb2eec-6160-11e5-9116-16d60c122eee.gif

.. |Bump Patch Version GIF|  image:: https://cloud.githubusercontent.com/assets/1279644/10024588/9ce09044-6160-11e5-81e1-b2c4d743b137.gif

.. |Bump Minor Version GIF|  image:: https://cloud.githubusercontent.com/assets/1279644/10024587/9ce077f8-6160-11e5-9252-4a154ac4734d.gif

.. |Bump Major Version GIF|  image:: https://cloud.githubusercontent.com/assets/1279644/10024583/9ca330fa-6160-11e5-962e-ec63bef155fd.gif


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



Change Logs
===========

0.6.0(Stable)
-------------

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

