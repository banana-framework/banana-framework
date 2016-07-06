# -*- encoding: utf-8 -*-
from __future__ import absolute_import

from pluggy import HookspecMarker

hookspec = HookspecMarker('banana')


@hookspec
def banana_register_commands(registry):
    """
    :param registry:
    :return:
    """


@hookspec
def banana_cmdline_run(xom):
    """ Returns an integer with a success code (0 == no errors) if
    you handle the command line invocation, otherwise None.

    :param xom:
    :return:
    """
