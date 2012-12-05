#!/usr/bin/env python
#
# Author: Endre Karlson
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
import textwrap
from setuptools import setup, find_packages
from fakturo.core.openstack.common import setup as common_setup
from fakturo.core.version import version_info as version

install_requires = common_setup.parse_requirements(['tools/pip-requires'])
tests_require = common_setup.parse_requirements(['tools/test-requires'])
setup_require = common_setup.parse_requirements(['tools/setup-requires'])
dependency_links = common_setup.parse_dependency_links([
    'tools/pip-requires',
    'tools/test-requires',
    'tools/setup-requires'
])

setup(
    name='python-fakturo',
    version=version.canonical_version_string(always=True),
    description='A provider of bindings / CLI commands for billingsystems',
    author='Endre Karlson',
    author_email='endre.karlson@gmail.com',
    url='https://github.com/billingstack/fakturo',
    namespace_packages=['fakturo'],
    packages=find_packages(exclude=['bin']),
    include_package_data=True,
    test_suite='nose.collector',
    setup_requires=setup_require,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    dependency_links=dependency_links,
    scripts=[
        'bin/fakturo',
    ],
    cmdclass=common_setup.get_cmdclass(),
    entry_points=textwrap.dedent("""
        [fakturo.core.cli]
        provider-list = fakturo.core.cli.provider:ListProviders

        merchant-create = fakturo.core.cli.merchant:MerchantCreate
        merchant-list = fakturo.core.cli.merchant:MerchantList
        merchant-get = fakturo.core.cli.merchant:MerchantGet
        merchant-update = fakturo.core.cli.merchant:MerchantUpdate
        merchant-delete = fakturo.core.cli.merchant:MerchantDelete
    """),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Finance :: Billing',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'Environment :: OpenStack',
    ],
)
