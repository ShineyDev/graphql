from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any
    from typing_extensions import Self

    from aiohttp import ClientResponse


class ClientError(Exception):
    """
    The base exception class for a GraphQL client.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    """

    __slots__ = ("message",)

    def __init__(
        self: Self,
        message: str,
    ) -> None:
        self.message: str = message

        super().__init__(message)


class ClientResponseError(ClientError):
    """
    Represents an error in a response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The client response.
    """

    __slots__ = ("response",)

    def __init__(
        self: Self,
        message: str,
        response: ClientResponse,
    ) -> None:
        self.response: ClientResponse = response

        super().__init__(f"{response.status}: {message}")


class ClientResponseGraphQLError(ClientResponseError):
    """
    Represents an error in a GraphQL response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The client response.
    data: :class:`dict`
        The response data.
    """

    __slots__ = ("data",)

    def __init__(
        self: Self,
        message: str,
        response: ClientResponse,
        data: dict[str, Any],
    ) -> None:
        self.data: dict[str, Any] = data

        super().__init__(message, response)


class ClientResponseHTTPError(ClientResponseError):
    """
    Represents an error in an HTTP response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The client response.
    data: Optional[:class:`dict`]
        The response data.
    """

    __slots__ = ("data",)

    def __init__(
        self: Self,
        message: str,
        response: ClientResponse,
        data: dict[str, Any] | None,
    ) -> None:
        self.data: dict[str, Any] | None = data

        super().__init__(message, response)


class ClientDeprecationWarning(DeprecationWarning):
    """
    Represents a :exc:`deprecation warning <DeprecationWarning>` from the GraphQL client.
    """

    __slots__ = ()


class ServerDeprecationWarning(DeprecationWarning):
    """
    Represents a :exc:`deprecation warning <DeprecationWarning>` from the GraphQL server.
    """

    __slots__ = ()


__all__ = [
    "ClientError",
    "ClientResponseError",
    "ClientResponseGraphQLError",
    "ClientResponseHTTPError",
    "ClientDeprecationWarning",
    "ServerDeprecationWarning",
]
