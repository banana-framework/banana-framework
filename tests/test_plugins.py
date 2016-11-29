from __future__ import absolute_import

from pluggy import PluginManager

from banana.pluggins.config import get_plugin_manager


def test_get_plugin_manager():
    pm = get_plugin_manager()
    assert isinstance(pm, PluginManager)
    assert pm.project_name == 'banana'
    assert pm._implprefix == 'banana_'
