from fakturo.core.cli.base import CreateCommand
from fakturo.core.cli.base import UpdateCommand
from fakturo.core.cli.base import DeleteCommand
from fakturo.core.cli.base import ListCommand
from fakturo.core.cli.base import GetCommand


class PaymentMethodCreate(CreateCommand):
    api = 'payment_method'


class PaymentMethodUpdate(UpdateCommand):
    api = 'payment_method'


class PaymentMethodDelete(DeleteCommand):
    api = 'payment_method'


class PaymentMethodList(ListCommand):
    api = 'payment_method'


class PaymentMethodGet(GetCommand):
    api = 'payment_method'
