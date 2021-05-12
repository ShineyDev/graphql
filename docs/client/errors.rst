.. currentmodule:: graphql.client


Errors
======

.. autoclass:: ClientError
    :members:

.. autoclass:: ClientResponseHTTPError
    :members:

.. autoclass:: ClientResponseGraphQLError
    :members:


.. code-block::

    Exception
     +-- ClientError
          +-- ClientResponseHTTPError
               +-- ClientResponseGraphQLError
