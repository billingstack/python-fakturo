#
# Author: Endre Karlson <endre.karlson@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from cliff.command import Command as CliffCommand
from cliff.lister import Lister
from cliff.show import ShowOne
from fakturo.core import utils


class Command(CliffCommand):
    api = None
    action = None

    @property
    def name(self):
        """
        The name of the command

        api-action like account-create
        """
        if self.api is None or self.action is None:
            return None
        return self.api + '-' + self.action

    @property
    def method_name(self):
        return self.name.replace('-', '_') if self.name else None

    def get_parser(self, prog_name):
        """
        Override get_parser in order to get equivelant from the Provider
        and extend options
        """
        parser = super(Command, self).get_parser(prog_name)
        self.app.provider_manager.extend_parser(self.method_name, parser)
        return parser

    def execute(self, parsed_args):
        """
        Execute something, this is since we overload self.take_action()
        in order to format the data

        :param parsed_args: The parsed args that are given by take_action()
        """
        return self.app.provider_manager.execute(
            self.method_name,
            parsed_args,
            self)

    def post_execute(self, data):
        """
        Format the results locally if needed, by default we just return data

        :param data: Whatever is returned by self.execute()
        """
        return data

    def take_action(self, parsed_args):
        """
        Call self.execute to get data and then format it a bit with post_exec
        """
        # TODO: Common Exception Handling Here
        results = self.execute(parsed_args)
        return self.post_execute(results)


class ListCommand(Command, Lister):
    action = 'list'

    def post_execute(self, results):
        if len(results) > 0:
            columns = utils.get_columns(results)
            data = [utils.get_item_properties(i, columns) for i in results]
            return columns, data
        else:
            return [], ()


class GetCommand(Command, ShowOne):
    action = 'get'

    def post_execute(self, results):
        return results.keys(), results.values()


class CreateCommand(Command, ShowOne):
    action = 'create'

    def post_execute(self, results):
        return results.keys(), results.values()


class UpdateCommand(Command, ShowOne):
    action = 'update'

    def post_execute(self, results):
        return results.keys(), results.values()


class DeleteCommand(Command):
    action = 'delete'


__all__ = ["Command", "ListCommand", "GetCommand", "CreateCommand",
           "UpdateCommand", "DeleteCommand"]
