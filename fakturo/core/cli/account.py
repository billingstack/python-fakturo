from fakturo.core.cli.base import CreateCommand
from fakturo.core.cli.base import UpdateCommand
from fakturo.core.cli.base import DeleteCommand
from fakturo.core.cli.base import ListCommand
from fakturo.core.cli.base import GetCommand


class AccountCreate(CreateCommand):
    api = 'account'


class AccountUpdate(UpdateCommand):
    api = 'account'


class AccountDelete(DeleteCommand):
    api = 'account'


class AccountList(ListCommand):
    api = 'account'


class AccountGet(GetCommand):
    api = 'account'
