.. currentmodule:: graphql.client.errors


Errors
======

.. autoclass:: ClientError()
    :members:

.. autoclass:: ClientResponseError()
    :members:

.. autoclass:: ClientResponseHTTPError()
    :members:

.. autoclass:: ClientResponseGraphQLError()
    :members:


Hierarchy
---------

.. code-block::

    Exception
     +-- ClientError
          +-- ClientResponseError
               +-- ClientResponseHTTPError
               +-- ClientResponseGraphQLError
