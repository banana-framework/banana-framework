from __future__ import absolute_import

import banana
from banana.utils.version import VersionInfo, semantic_version


def test_utils_version():
    v = VersionInfo(1, 2, 3, 'alpha', 10)
    version = semantic_version(v)
    assert version == '1.2.3a10'
    assert version == v.semantic_version

    banana.VERSION = VersionInfo(1, 0, 0, 'final', 0)
    version = semantic_version()
    assert version == '1.0.0'
    assert version == banana.VERSION.semantic_version
