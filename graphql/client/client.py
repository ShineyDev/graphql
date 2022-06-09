from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any
    from typing_extensions import Self

    from aiohttp import ClientSession

from graphql.client.http import HTTPClient


class Client:
    """
    The base class for a GraphQL client.

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
        /,
        *,
        session: ClientSession,
        url: str,
    ) -> None:
        self._http = HTTPClient(session, url)

    async def request(
        self: Self,
        document_: str,
        operation_: str | None = None,
        /,
        **variables: Any,
    ) -> dict[str, Any]:
        """
        |coro|

        Sends a request to a GraphQL server.

        Parameters
        ----------
        document_: :class:`str`
            A GraphQL document.

            .. tip::

                If you haven't already, you should |graphql_learn|.
        operation_: :class:`str`
            The name of the operation from the document to execute.
        **variables: Any
            A mapping of GraphQL variables.

        Raises
        ------
        ~graphql.client.ClientResponseHTTPError
            Arbitrary HTTP error.
        ~graphql.client.ClientResponseGraphQLError
            Arbitrary GraphQL error.


        :rtype: :class:`dict`
        """

        return await self._http.request(document_, operation_, variables)


__all__ = [
    "Client",
]
