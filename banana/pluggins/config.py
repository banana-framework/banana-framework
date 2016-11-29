# -*- encoding: utf-8 -*-
from __future__ import absolute_import

from pluggy import PluginManager

from . import hookspecs


def get_plugin_manager(load_entrypoints=True):
    pm = PluginManager('banana', implprefix='banana_')
    pm.add_hookspecs(hookspecs)
    if load_entrypoints:
        pm.load_setuptools_entrypoints('banana')
    pm.check_pending()
    return pm