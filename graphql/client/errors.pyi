from typing import Optional

from aiohttp import ClientResponse


class ClientError(Exception):
    message: str


class ClientResponseError(ClientError):
    response: ClientResponse


class ClientResponseHTTPError(ClientResponseError):
    data: Optional[dict]


class ClientResponseGraphQLError(ClientResponseError):
    data: dict


class ClientResponseGraphQLValidationError(ClientResponseGraphQLError):
    pass
