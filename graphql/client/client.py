from .http import HTTPClient


class Client:
    """
    The base class for interaction with a GraphQL API.

    Parameters
    ----------
    session: :class:`aiohttp.ClientSession`
        A client session.
    url: :class:`str`
        A URL the the GraphQL API.
    """

    __slots__ = ("_http",)

    def __init__(self, *, session, url):
        self._http = HTTPClient(session, url)

    async def request(self, document, operation=None, **variables):
        """
        |coro|

        Sends a request to a GraphQL API.

        Parameters
        ----------
        document: :class:`str`
            A GraphQL document.

            .. tip::

                If you haven't already, you should |graphql_learn|_.
        operation: :class:`str`
            The name of the operation from the document to execute.
        **variables
            A mapping of GraphQL variables.

        Raises
        ------
        ~graphql.client.errors.ClientResponseHTTPError
            Arbitrary HTTP error.
        ~graphql.client.errors.ClientResponseGraphQLError
            Arbitrary GraphQL error.


        :rtype: :class:`dict`
        """

        return await self._http.request(document, operation, variables)


__all__ = [
    "Client",
]
