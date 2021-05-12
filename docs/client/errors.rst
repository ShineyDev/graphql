.. currentmodule:: graphql.client


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


.. code-block::

    Exception
     +-- ClientError
          +-- ClientResponseError
               +-- ClientResponseHTTPError
               +-- ClientResponseGraphQLError
