from __future__ import absolute_import

import os
import sys

from argparse import ArgumentParser

from banana import VERSION
from banana.app import app


class CommandError(Exception):
    """
    Exception class indicating a problem while executing a management
    command.
    If this exception is raised during the execution of a management
    command, it will be caught and turned into a nicely-printed error
    message to the appropriate output stream (i.e., stderr); as a
    result, raising this exception (with a sensible description of the
    error) is the preferred way to indicate that something has gone
    wrong in the execution of a command.
    """
    pass


def handle_default_options(options):
    """
    Include any default options that all commands should accept here
    so that ManagementUtility can handle them before searching for
    user commands.
    """
    if options.settings:
        os.environ['BANANA_SETTINGS'] = options.settings
    if options.pythonpath:
        sys.path.insert(0, options.pythonpath)


class CommandParser(ArgumentParser):
    """
    Customized ArgumentParser class to improve some error messages and prevent
    SystemExit in several occasions, as SystemExit is unacceptable when a
    command is called programmatically.
    """
    def __init__(self, cmd, **kwargs):
        self.cmd = cmd
        super(CommandParser, self).__init__(**kwargs)

    def parse_args(self, args=None, namespace=None):
        # Catch missing argument for a better error message
        if (hasattr(self.cmd, 'missing_args_message') and
                not (args or any(not arg.startswith('-') for arg in args))):
            self.error(self.cmd.missing_args_message)
        return super(CommandParser, self).parse_args(args, namespace)

    def error(self, message):
        if self.cmd._called_from_command_line:
            super(CommandParser, self).error(message)
        else:
            raise CommandError("Error: %s" % message)


class ManagementUtility(object):
    def __init__(self, argv=None):
        self.app = app
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        self.settings_exception = None

    def main_help_text(self, commands_only=False):
        """
        Returns the script's main help text, as a string.
        """
        if commands_only:
            usage = self.app.commands
        else:
            usage = [
                "",
                "Type '%s help <subcommand>' for help on a specific"
                " subcommand." % self.prog_name,
                "",
                "Available subcommands:",
            ]

        return '\n'.join(usage)

    def execute(self):
        try:
            subcommand = self.argv[1]
        except IndexError:
            subcommand = 'help'  # Display help if no arguments were given.

        parser = CommandParser(
            None, usage='%(prog)s subcommand [options] [args]', add_help=False
        )
        parser.add_argument('--settings')
        parser.add_argument('--pythonpath')
        parser.add_argument('args', nargs='*')

        try:
            options, args = parser.parse_known_args(self.argv[2:])
            handle_default_options(options)
        except CommandError:
            options = None
            args = []
            pass  # Ignore any option errors at this point.

        if subcommand == 'help':
            if '--commands' in args:
                sys.stdout.write(
                    self.main_help_text(commands_only=True) + '\n')
            elif len(options.args) < 1:
                sys.stdout.write(self.main_help_text() + '\n')
            else:
                self.fetch_command(options.args[0]).print_help(self.prog_name,
                                                               options.args[0])
        elif subcommand == 'version' or self.argv[1:] == ['--version']:
            sys.stdout.write(VERSION.semantic_version + '\n')
        elif self.argv[1:] in (['--help'], ['-h']):
            sys.stdout.write(self.main_help_text() + '\n')
        else:
            self.fetch_command(subcommand).run_from_argv(self.argv)


def execute_from_command_line(argv=None):
    """
    A simple method that runs a ManagementUtility.
    """
    utility = ManagementUtility(argv)
    utility.execute()

if __name__ == '__main__':
    execute_from_command_line()
