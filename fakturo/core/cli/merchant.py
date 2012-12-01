from fakturo.cli.base import CreateCommand
from fakturo.cli.base import UpdateCommand
from fakturo.cli.base import DeleteCommand
from fakturo.cli.base import ListCommand
from fakturo.cli.base import GetCommand


class CreateMerchant(CreateCommand):
    def get_parser(self, prog_name):
        parser = super(CreateMerchant, self).get_parser(prog_name)
        return parser


class UpdateMerchant(UpdateCommand):
    def get_parser(self, prog_name):
        parser = super(UpdateMerchant, self).get_parser(prog_name)
        return parser


class DeleteMerchant(DeleteCommand):
    def get_parser(self, prog_name):
        parser = super(DeleteMerchant, self).get_parser(prog_name)
        return parser


class ListMerchants(ListCommand):
    def get_parser(self, prog_name):
        parser = super(ListMerchants, self).get_parser(prog_name)
        return parser


class GetMerchant(GetCommand):
    def get_parser(self, prog_name):
        parser = super(GetMerchant, self).get_parser(prog_name)
        return parser
