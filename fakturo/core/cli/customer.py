from fakturo.core.cli.base import CreateCommand
from fakturo.core.cli.base import UpdateCommand
from fakturo.core.cli.base import DeleteCommand
from fakturo.core.cli.base import ListCommand
from fakturo.core.cli.base import GetCommand


class CustomerCreate(CreateCommand):
    api = 'customer'


class CustomerUpdate(UpdateCommand):
    api = 'customer'


class CustomerDelete(DeleteCommand):
    api = 'customer'


class CustomerList(ListCommand):
    api = 'customer'


class CustomerGet(GetCommand):
    api = 'customer'
