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
    url='https://github.com/ekarlso/fakturo',
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

        account-create = fakturo.core.cli.account:AccountCreate
        account-list = fakturo.core.cli.account:AccountList
        account-get = fakturo.core.cli.account:AccountGet
        account-update = fakturo.core.cli.account:AccountUpdate
        account-delete = fakturo.core.cli.account:AccountDelete

        customer-create = fakturo.core.cli.customer:CustomerCreate
        customer-list = fakturo.core.cli.customer:CustomerList
        customer-get = fakturo.core.cli.customer:CustomerGet
        customer-update = fakturo.core.cli.customer:CustomerUpdate
        customer-delete = fakturo.core.cli.customer:CustomerDelete

        pm-create = fakturo.core.cli.paymentmethod:PaymentMethodCreate
        pm-list = fakturo.core.cli.paymentmethod:PaymentMethodList
        pm-get = fakturo.core.cli.paymentmethod:PaymentMethodGet
        pm-update = fakturo.core.cli.paymentmethod:PaymentMethodUpdate
        pm-delete = fakturo.core.cli.paymentmethod:PaymentMethodDelete

        plan-create = fakturo.core.cli.plan:PlanCreate
        plan-list = fakturo.core.cli.plan:PlanList
        plan-get = fakturo.core.cli.plan:PlanGet
        plan-update = fakturo.core.cli.plan:PlanUpdate
        plan-delete = fakturo.core.cli.plan:PlanDelete

        product-create = fakturo.core.cli.product:ProductCreate
        product-list = fakturo.core.cli.product:ProductList
        product-get = fakturo.core.cli.product:ProductGet
        product-update = fakturo.core.cli.product:ProductUpdate
        product-delete = fakturo.core.cli.product:ProductDelete

        subscription-create = fakturo.core.cli.subscription:SubscriptionCreate
        subscription-list = fakturo.core.cli.subscription:SubscriptionList
        subscription-get = fakturo.core.cli.subscription:SubscriptionGet
        subscription-update = fakturo.core.cli.subscription:SubscriptionUpdate
        subscription-delete = fakturo.core.cli.subscription:SubscriptionDelete
   """),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Finance :: Billing',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console'
    ],
)
