DEPRECATED don't use it. Please do::

    import importlib
    foopath = 'src.apis.foo.Foo'

    module_name = '.'.join(foopath.split('.')[:-1]) # to get src.apis.foo
    foo_module = importlib.import_module(module_name)
    clazz_name = foopath.split('.')[-1] # to get Foo
    Foo = getattr(module_name, clazz_name)
    print Foo()


=============
import_string
=============


.. image:: https://img.shields.io/pypi/v/import_string.svg
        :target: https://pypi.python.org/pypi/import_string

.. image:: https://img.shields.io/travis/rochacbruno/import_string.svg
        :target: https://travis-ci.org/rochacbruno/import_string

.. image:: https://readthedocs.org/projects/import-string/badge/?version=latest
        :target: https://import-string.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/rochacbruno/import_string/shield.svg
     :target: https://pyup.io/repos/github/rochacbruno/import_string/
     :alt: Updates


Imports an object based on a string


* Free software: ISC license
* Documentation: https://import-string.readthedocs.io.


Features
--------

Imports an object based on a string.  This is useful if you want to
use import paths as endpoints or something similar.  An import path can
be specified either in dotted notation (``.``)
or with a colon as object delimiter (``:``).
If `silent` is True the return value will be `None` if the import fails.

Usage
-----

.. code-block:: python

    import import_string

    module = import_string('my_system.my_package.my_module')

    function = import_string('my_system.my_module:some_function')

    Class = import_string('my_system.my_module:SomeClass', silent=True)
    # If path doesn't exist Class = None


Live demo
---------

See it in action here: https://repl.it/EGdS/0

Credits
-------

- This package was extracted from `werkzeug.utils` module
- This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

