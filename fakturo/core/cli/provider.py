from fakturo.core.cli.base import ListCommand
from fakturo.core.provider import list_providers


class ListProviders(ListCommand):
    """
    List all available Providers
    """
    def execute(self, parsed_args):
        return list_providers()