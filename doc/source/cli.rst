..
    Copyright 2012 Endre Karlson for Bouvet ASA

    Licensed under the Apache License, Version 2.0 (the "License"); you may
    not use this file except in compliance with the License. You may obtain
    a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations
    under the License.

.. _cli:

========================
Command Line Interface
========================

.. note::
   The CLI of Fakturo proxies onto a Provider's CMD object which does the heavy
   lifting. We provide a standard set of commands in addition to the providers
   own defined commands.

========
Commands
========

Merchant
++++++++

Create
======

.. code-block:: bash

   test

List
====

.. code-block:: bash

   fakturo merchant-list ...

Get
===

.. code-block:: bash

   fakturo merchant-create ...

Update
======

.. code-block:: bash

   fakturo merchant-get ...

Delete
======

.. code-block:: bash

   fakturo merchant-delete ...
