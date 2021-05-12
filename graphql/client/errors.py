class ClientError(Exception):
    """
    The base exception class for the GraphQL client.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    """

    __slots__ = ("message",)

    def __init__(self, message):
        self.message = message

        super().__init__(message)


class ClientResponseHTTPError(ClientError):
    """
    Represents an error in an HTTP response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The HTTP response.
    data: Optional[:class:`dict`]
        The response data.
    """

    __slots__ = ("response", "data")

    def __init__(self, message, response, data):
        self.response = response
        self.data = data

        super().__init__(f"{response.status}: {message}")


class ClientResponseGraphQLError(ClientResponseHTTPError):
    """
    Represents an error in a GraphQL response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The HTTP response.
    data: :class:`dict`
        The response data.
    """

    __slots__ = ()


__all__ = [
    "ClientError",
    "ClientResponseHTTPError",
    "ClientResponseGraphQLError",
]
