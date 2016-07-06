from __future__ import absolute_import

import banana
from banana.utils.version import VersionInfo, get_version


def test_utils_version():
    version = get_version(VersionInfo(1, 2, 3, 'alpha', 10))
    assert version == '1.2.3a10'
    banana.VERSION = VersionInfo(1, 0, 0, 'final', 0)
    version = get_version()
    assert version == '1.0.0'
