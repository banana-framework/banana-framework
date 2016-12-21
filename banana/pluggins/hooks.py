# -*- encoding: utf-8 -*-
from __future__ import absolute_import

from pluggy import HookimplMarker, HookspecMarker


hook_spec = HookspecMarker('banana')
hook_impl = HookimplMarker('banana')


@hook_spec
def banana_on_app_initialize(app):
    """

    :param app:
    :return:
    """


@hook_spec
def banana_register_commands(registry):
    """
    :param registry:
    :return:
    """


@hook_spec
def banana_cmdline_run(xom):
    """ Returns an integer with a success code (0 == no errors) if
    you handle the command line invocation, otherwise None.

    :param xom:
    :return:
    """
