from stevedore.driver import DriverManager


"""
This loads up the Provider which is the implementation of the billing system
"""


NAMESPACE = 'fakturo.provider'


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

    def get_provider(self):
        """
        Get a provider based on the self.provider_name propery
        """
        mgr = DriverManager(
            NAMESPACE,
            self.provider,
            invoke_on_load=True)
        return mgr.driver

    def execute(self, name, parsed_args, command):
        """
        Execute the command by name from a Provider

        :param name: Name of the command
        :param parsed_args: Parsed arguments
        :param command: The command name to run

        :return: The results of the Provider's command.
        """
        provider = self.get_provider()
        api = provider.get_api(parsed_args, command)
        return getattr(api, name)(parsed_args, command)

    def extend_parser(self, name, parser):
        """
        Extend the parser for the Command from the Provider

        :param name: Name of the command
        :param parser: The Parser object
        """
        provider = self.get_provider()
        provider.extend_parser(name, parser)
