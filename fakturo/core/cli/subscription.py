from fakturo.core.cli.base import CreateCommand
from fakturo.core.cli.base import UpdateCommand
from fakturo.core.cli.base import DeleteCommand
from fakturo.core.cli.base import ListCommand
from fakturo.core.cli.base import GetCommand


class SubscriptionCreate(CreateCommand):
    api = 'subscription'


class SubscriptionUpdate(UpdateCommand):
    api = 'subscription'


class SubscriptionDelete(DeleteCommand):
    api = 'subscription'


class SubscriptionList(ListCommand):
    api = 'subscription'


class SubscriptionGet(GetCommand):
    api = 'subscription'
