.. currentmodule:: graphql.client.errors


Errors
======

.. autoclass:: ClientError()
    :members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseError()
    :members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseHTTPError()
    :members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseGraphQLError()
    :members:
    :exclude-members: with_traceback


Hierarchy
---------

.. code-block::

    Exception
     +-- ClientError
          +-- ClientResponseError
               +-- ClientResponseHTTPError
               +-- ClientResponseGraphQLError
