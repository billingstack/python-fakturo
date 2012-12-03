from fakturo.core.cli.base import ListCommand


class ListProviders(ListCommand):
    has_client = False

    def execute(self, parsed_args):
        return {}
