.. raw:: html

    <p align="center">
        <a href="https://github.com/ShineyDev/graphql/actions/workflows/analyze.yml?query=branch%3Amain+event%3Apush"><img alt="Analyze Status" src="https://github.com/ShineyDev/graphql/actions/workflows/analyze.yml/badge.svg?branch=main&event=push" /></a>
        <a href="https://github.com/ShineyDev/graphql/actions/workflows/build.yml?query=branch%3Amain+event%3Apush"><img alt="Build Status" src="https://github.com/ShineyDev/graphql/actions/workflows/build.yml/badge.svg?branch=main&event=push" /></a>
        <a href="https://github.com/ShineyDev/graphql/actions/workflows/check.yml?query=branch%3Amain+event%3Apush"><img alt="Check Status" src="https://github.com/ShineyDev/graphql/actions/workflows/check.yml/badge.svg?branch=main&event=push" /></a>
        <a href="https://github.com/ShineyDev/graphql/actions/workflows/deploy.yml?query=branch%3Amain+event%3Apush"><img alt="Deploy Status" src="https://github.com/ShineyDev/graphql/actions/workflows/deploy.yml/badge.svg?branch=main&event=push" /></a>
        <a href="https://github.com/ShineyDev/graphql/actions/workflows/lint.yml?query=branch%3Amain+event%3Apush"><img alt="Lint Status" src="https://github.com/ShineyDev/graphql/actions/workflows/lint.yml/badge.svg?branch=main&event=push" /></a>
    </p>

----------

.. raw:: html

    <h1 align="center">ShineyDev/graphql</h1>
    <p align="center">An asynchronous Python library for interaction with GraphQL APIs.<br><a href="https://github.com/ShineyDev/graphql">source</a> | <a href="https://docs.shiney.dev/graphql">documentation</a></p>


Install
-------

.. pull-quote::

    [!WARNING]

    This installation may be unstable. If you're looking for a stable release, go `here <https://github.com/ShineyDev/graphql/tags>`_.

.. code:: shell

    $ python -m pip install --upgrade git+https://github.com/ShineyDev/graphql.git@main


There is also a more in-depth `installation guide <https://docs.shiney.dev/graphql/latest/guide/installation>`_ in the documentation.


Use
---

.. code:: python

    >>> import aiohttp
    >>> import graphql
    >>>
    >>> session = aiohttp.ClientSession()
    >>> client = graphql.client.Client(session=session, url="https://swapi-graphql.netlify.app/.netlify/functions/index/graphql")
    >>>
    >>> await client.request("{allPeople(first:3){edges{node{name}}}}")
    {'allPeople': {'edges': [{'node': {'name': 'Luke Skywalker'}}, {'node': {'name': 'C-3PO'}}, {'node': {'name': 'R2-D2'}}]}}


There are also more in-depth `usage guides <https://docs.shiney.dev/graphql/latest/guide/use>`_ in the documentation.


.. raw:: html

    <h6 align="center">Copyright 2021-present ShineyDev<br>This repository is not endorsed by or affiliated with The GraphQL Foundation or its affiliates. "GraphQL" is a registered trademark of The GraphQL Foundation.</h6>
