from fakturo.core.cli.base import CreateCommand
from fakturo.core.cli.base import UpdateCommand
from fakturo.core.cli.base import DeleteCommand
from fakturo.core.cli.base import ListCommand
from fakturo.core.cli.base import GetCommand


class MerchantCreate(CreateCommand):
    api = 'merchant'


class MerchantUpdate(UpdateCommand):
    api = 'merchant'


class MerchantDelete(DeleteCommand):
    api = 'merchant'


class MerchantList(ListCommand):
    api = 'merchant'


class MerchantGet(GetCommand):
    api = 'merchant'
