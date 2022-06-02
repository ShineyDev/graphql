from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any
    from typing_extensions import Self

    from aiohttp import ClientSession

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

    def __init__(
        self: Self,
        *,
        session: ClientSession,
        url: str,
    ) -> None:
        self._http = HTTPClient(session, url)

    async def request(
        self: Self,
        document: str,
        operation: str | None = None,
        **variables: Any,
    ) -> dict:
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
