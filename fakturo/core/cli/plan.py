from fakturo.core.cli.base import CreateCommand
from fakturo.core.cli.base import UpdateCommand
from fakturo.core.cli.base import DeleteCommand
from fakturo.core.cli.base import ListCommand
from fakturo.core.cli.base import GetCommand


class PlanCreate(CreateCommand):
    api = 'plan'


class PlanUpdate(UpdateCommand):
    api = 'plan'


class PlanDelete(DeleteCommand):
    api = 'plan'


class PlanList(ListCommand):
    api = 'plan'


class PlanGet(GetCommand):
    api = 'plan'
