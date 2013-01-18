from fakturo.core.cli.base import CreateCommand
from fakturo.core.cli.base import UpdateCommand
from fakturo.core.cli.base import DeleteCommand
from fakturo.core.cli.base import ListCommand
from fakturo.core.cli.base import GetCommand


class ProductCreate(CreateCommand):
    api = 'product'


class ProductUpdate(UpdateCommand):
    api = 'product'


class ProductDelete(DeleteCommand):
    api = 'product'


class ProductList(ListCommand):
    api = 'product'


class ProductGet(GetCommand):
    api = 'product'
