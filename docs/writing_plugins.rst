.. _plugins:
.. _`writing-plugins`:


.. _`setuptools entry points`:
.. _`pip-installable plugins`:

Making your plugin installable by others
----------------------------------------

To make your plugin, you have to define an entry point for your distribution.
``Banana`` uses standard `(pluggy) <https://github.com/pytest-dev/pluggy>`_
features for this purposes.

.. sourcecode:: python

    # sample ./setup.py file
    from setuptools import setup

    setup(
        name="myproject",
        packages = ['myproject']

        # the following makes a plugin available to banana
        entry_points = {
            'banana': [
                'name_of_plugin = myproject.pluginmodule',
            ]
        },

        # custom PyPI classifier for banana plugins
        classifiers=[
            "Framework :: Banana",
        ],
    )

.. note::

    Make sure to include ``Framework :: Banana`` in your list of
    `PyPI classifiers <https://python-packaging-user-guide.readthedocs.io/en/latest/distributing/#classifiers>`_
    to make it easy for users to find your plugin.
