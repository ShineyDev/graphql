from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any
    from typing_extensions import Self

    from aiohttp import ClientSession

import aiohttp

import graphql


class HTTPClient:
    __slots__ = ("session", "url")

    def __init__(
        self: Self,
        session: ClientSession,
        url: str,
    ) -> None:
        self.session: ClientSession = session
        self.url: str = url

    async def request(
        self: Self,
        document_: str,
        operation_: str | None,
        variables_: dict[str, Any] | None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        # region internal

        _data_validate = kwargs.pop("_data_validate", None)

        # endregion

        json = kwargs.pop("json", None) or dict()

        # NOTE: The GraphQL specification is not able to mandate HTTP
        #       parameters, but the following is described as standard
        #       on GraphQL.org.
        #
        #       > A standard GraphQL POST request should use the
        #         application/json content type, and include a
        #         JSON-encoded body of the following form:
        #
        #         {
        #           "query": "...",
        #           "operationName": "...",
        #           "variables": { ... }
        #         }
        #
        #         operationName and variables are optional fields.
        #         operationName is only required if multiple operations
        #         are present in the query.

        json["query"] = document_

        if operation_:
            json["operationName"] = operation_

        if variables_:
            json["variables"] = variables_

        # NOTE: The GraphQL specification is not able to mandate HTTP
        #       methods, but GET and POST are the only methods
        #       described as standard on GraphQL.org.
        #
        #       > Your GraphQL HTTP server should handle the HTTP GET
        #         and POST methods.

        try:
            async with self.session.post(self.url, json=json, **kwargs) as response:
                if not 200 <= response.status < 300:
                    # NOTE: The GraphQL specification is not able to
                    #       mandate HTTP status, but this block is pretty
                    #       standard AFAIA.

                    message: str

                    try:
                        data = await response.json()
                        message = data["message"]
                    except (aiohttp.ContentTypeError, KeyError):
                        data = None
                        message = response.reason  # type: ignore

                    raise graphql.client.ClientResponseHTTPError(message, response, data)

                # NOTE: While the GraphQL specification does not mandate a
                #       serialization format, JSON is by far the most
                #       common response serialization for GraphQL servers.

                data = await response.json()
        except aiohttp.ClientResponseError as e:
            raise graphql.client.ClientResponseError(e.message, response) from e  # pyright: ignore[reportUnboundVariable]
        except aiohttp.ClientError as e:
            raise graphql.client.ClientError(str(e)) from e
        else:
            # NOTE: The GraphQL specification mandates that the
            #       "errors" key must (and must only) exist when the
            #       operation encounters an error. The following block
            #       is extra careful about an empty array anyway.
            #
            #       > If the operation encountered any errors, the
            #       response map must contain an entry with key errors.
            #       [...] If the operation completed without
            #       encountering any errors, this entry must not be
            #       present.

            try:
                errors = data["errors"]
            except KeyError:
                errors = None

            if errors:
                exceptions = list()

                for error in errors:
                    # NOTE: The GraphQL specification mandates that
                    #       every error must provide a "message" key.
                    #
                    #       > Every error must contain an entry with
                    #         the key message with a string description
                    #         of the error intended for the developer
                    #         as a guide to understand and correct the
                    #         error.

                    message = error["message"]

                    exceptions.append(graphql.client.ClientResponseGraphQLError(message, response, data))

                if False:  # len(exceptions) > 1:
                    # TODO: I'm not sure I love this interface.
                    raise ClientResponseGraphQLErrorCollection(exceptions)
                else:
                    raise exceptions[0]

            # region internal

            if _data_validate is not None:
                _data_validate(response, data)

            # endregion

            # NOTE: The GraphQL specification mandates that the "data" key
            #       must be present when no error is encountered.
            #
            #       > If the data entry in the response is not present, the
            #         errors entry in the response must not be empty. It
            #         must contain at least one error. The errors it
            #         contains should indicate why no data was able to be
            #         returned.

            return data["data"]


__all__ = [
    "HTTPClient",
]
