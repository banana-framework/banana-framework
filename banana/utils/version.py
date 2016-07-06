# -*- encoding: utf-8 -*-
from __future__ import absolute_import

from collections import namedtuple

_VersionInfoBase = namedtuple(
    'VersionInfo', ('major', 'minor', 'micro', 'status', 'build')
)


class VersionInfo(_VersionInfoBase):
    """Version Info structure for semantic versions

    :param major: major index
    :type major: int
    :param minor: minor index
    :type minor: int
    :param micro: micro index
    :type micro: int
    :param status: status code (`alpha`, `beta`, `rc`, `final`) default is \
    `final`
    :type status: str
    :param build: build number
    :type build: int
    """
    __slots__ = ()


STATUS_MAPPING = {
    'alpha': 'a',
    'beta': 'b',
    'rc': 'rc',
    'final': '',
}


def get_version(version=None):
    """Returns semantic version representation `(PEP-440)
    <https://www.python.org/dev/peps/pep-0440/>`_

    :param version: structured version. By default :py:const:`banana.VERSION`
    :type version: :py:class:`VersionInfo`
    :return: semantic version representation
    :rtype: str

    Examples:
        >>> from banana.utils.version import VersionInfo, get_version
        >>> version = VersionInfo(0, 1, 2, 'beta', 10)
        >>> get_version(version)
        '0.1.2b10'

        >>> from banana.utils.version import VersionInfo, get_version
        >>> version = VersionInfo(0, 1, 2, 'final', 10)
        >>> get_version(version)
        '0.1.2'

        >>> from banana import VERSION
        >>> from banana.utils.version import VersionInfo, get_version
        >>> get_version() == get_version(VERSION)
        True
    """
    if version is None:
        from banana import VERSION
        version = VERSION
    main_version = '{0.major}.{0.minor}.{0.micro}'.format(version)
    postfix = ''
    status = STATUS_MAPPING[version.status]
    if status:
        postfix = '{0}{1.build}'.format(status, version)
    return main_version + postfix
