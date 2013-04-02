from fakturo.core.exceptions import CommandNotSupported
from fakturo.core.provider import get_provider


"""
This loads up the Provider which is the implementation of the billing system
"""


class ProviderManager(object):
    """
    Helper that allows for Commands to "proxy" onto a Provider object
    """
    def __init__(self, app):
        self.app = app

    @property
    def provider(self):
        """
        Return the provider that's currently used
        """
        return self.app.options.provider

    def execute(self, name, parsed_args, command):
        """
        Execute the command by name from a Provider

        :param name: Name of the command
        :param parsed_args: Parsed arguments
        :param command: The command name to run

        :return: The results of the Provider's command.
        """
        provider = get_provider(self.provider)
        api = provider.get_api(parsed_args, command)

        try:
            command_func = getattr(api, name)
        except AttributeError:
            raise CommandNotSupported('Command is not supported by provider')
        return command_func(parsed_args, command)

    def extend_parser(self, name, parser):
        """
        Extend the parser for the Command from the Provider

        :param name: Name of the command
        :param parser: The Parser object
        """
        provider = get_provider(self.provider)
        provider.extend_parser(name, parser)
