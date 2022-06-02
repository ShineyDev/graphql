.. raw:: html

    <p align="center">
        <a href="https://github.com/ShineyDev/graphql/actions?query=branch%3Amain+event%3Apush+workflow%3AAnalyze">
            <img alt="Analyze Status" src="https://github.com/ShineyDev/graphql/workflows/Analyze/badge.svg?branch=main&event=push" />
        </a>

        <a href="https://github.com/ShineyDev/graphql/actions?query=branch%3Amain+event%3Apush+workflow%3ABuild">
            <img alt="Build Status" src="https://github.com/ShineyDev/graphql/workflows/Build/badge.svg?branch=main&event=push" />
        </a>

        <a href="https://github.com/ShineyDev/graphql/actions?query=branch%3Amain+event%3Apush+workflow%3ACheck">
            <img alt="Check Status" src="https://github.com/ShineyDev/graphql/workflows/Check/badge.svg?branch=main&event=push" />
        </a>

        <a href="https://github.com/ShineyDev/graphql/actions?query=branch%3Amain+event%3Apush+workflow%3ADeploy">
            <img alt="Deploy Status" src="https://github.com/ShineyDev/graphql/workflows/Deploy/badge.svg?branch=main&event=push" />
        </a>

        <a href="https://github.com/ShineyDev/graphql/actions?query=branch%3Amain+event%3Apush+workflow%3ALint">
            <img alt="Lint Status" src="https://github.com/ShineyDev/graphql/workflows/Lint/badge.svg?branch=main&event=push" />
        </a>
    </p>

----------

.. raw:: html

    <h1 align="center">ShineyDev/graphql</h1>
    <p align="center">An asynchronous Python library for interaction with GraphQL APIs.<br><a href="https://github.com/ShineyDev/graphql">source</a> | <a href="https://docs.shiney.dev/graphql">documentation</a></p>


Install
-------

.. code:: shell

    $ python -m pip install --upgrade git+https://github.com/ShineyDev/graphql.git@main


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


.. raw:: html

    <h6 align="center">Copyright 2021-present ShineyDev<br>This repository is not endorsed by or affiliated with The GraphQL Foundation or its affiliates. "GraphQL" is a registered trademark of The GraphQL Foundation.</h6>
