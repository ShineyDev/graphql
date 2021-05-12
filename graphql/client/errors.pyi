from typing import Optional

from aiohttp import ClientResponse


class ClientError(Exception):
    message: str


class ClientResponseHTTPError(ClientError):
    message: str
    response: ClientResponse
    data: Optional[dict]


class ClientResponseGraphQLError(ClientResponseHTTPError):
    message: str
    response: ClientResponse
    data: dict
