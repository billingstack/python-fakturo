from fakturo.core.cli.base import ListCommand


class ListProviders(ListCommand):
    """
    List all available Providers
    """
    def execute(self, parsed_args):
        return {}
