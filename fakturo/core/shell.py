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
import os
import logging
import pkg_resources
from cliff.app import App
from cliff.commandmanager import CommandManager, EntryPointWrapper

from fakturo.core import DESCRIPTION
from fakturo.core.provider.manager import ProviderManager
from fakturo.core.version import version_info


LOG = logging.getLogger(__name__)


class FakturoManager(CommandManager):
    """
    A CommandManager that uses multiple entrypoint namespaces for commands
    """
    def __init__(self, core_namespace, plugin_namespace=None):
        self.core_namespace = core_namespace
        self.namespaces = [core_namespace, plugin_namespace]

        self._commands = {}
        self._load_commands()

    def _load_commands(self):
        for ns in self.namespaces:
            if ns is None:
                continue
            LOG.debug("Scanning namespace for commands", ns)
            for ep in pkg_resources.iter_entry_points(ns):
                LOG.debug("Found command %r provided by %r", ep.name, ns)
                self.add_command_ep(ep, ns=ns)

    @property
    def commands(self):
        return self.get_commands()

    def add_command_ep(self, ep, ns=None):
        ns = ns or self.core_namespace
        if not ns in self._commands:
            self._commands[ns] = {}
        LOG.debug('Adding %s to ns %s', ep.name, ns)
        self._commands[ns][ep.name.replace('_', ' ')] = ep

    def add_command(self, name, command_class, ns=None):
        """
        Add a command from a Class, will be wrapped in EntryPointClass in
        order to look like a EntryPoint
        """
        ep = EntryPointWrapper(name, command_class)
        self.add_command_ep(ep, ns=ns)

    def get_commands(self, namespaces=None):
        namespaces = namespaces or self.namespaces
        commands = {}
        for ns in namespaces:
            if ns is None:
                continue
            for name, ep in self._commands[ns].items():
                # NOTE: In order to debug plugin commands overriding default
                # ones
                if name in commands:
                    LOG.debug("Command %r is already defined but %r overrides",
                              name, ns)
                commands[name] = ep
        return commands

    def __iter__(self):
        return iter(self.commands.items())


class FakturoShell(App):
    """
    A Proxy'ing shell that uses commands from other libraries provided by
    fakturo.provider.libraryx
    """
    def __init__(self):
        super(FakturoShell, self).__init__(
            description=DESCRIPTION,
            version=version_info,
            command_manager=CommandManager('fakturo.core.cli')
        )

        self.provider_manager = ProviderManager(self)

    def build_option_parser(self, description, version, argparse_kwargs=None):
        parser = super(FakturoShell, self).build_option_parser(
            description, version, argparse_kwargs)

        parser.add_argument('--api-url',
                            default=os.environ.get('FAKTURO_API_URL'),
                            type=str,
                            help="The API endpoint to interact with")

        provider = os.environ.get('FACTURO_PROVIDER', 'billingstack')
        parser.add_argument('--provider', default=provider,
                            help='Whcih provider to use')
        return parser
