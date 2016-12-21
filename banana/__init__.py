# -*- encoding: utf-8 -*-
from __future__ import absolute_import

from banana.utils.version import VersionInfo


VERSION = VersionInfo(
    0, 0, 1, 'alpha', 0
)

__version__ = VERSION.semantic_version
