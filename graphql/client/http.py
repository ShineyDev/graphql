import aiohttp

import graphql


class HTTPClient:
    __slots__ = ("session", "url")

    def __init__(self, session, url):
        self.session = session
        self.url = url

    async def request(self, __document, __operation, __variables, **kwargs):
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

        json["query"] = __document

        if __operation:
            json["operationName"] = __operation

        if __variables:
            json["variables"] = __variables

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

                    try:
                        data = await response.json()
                        message = data["message"]
                    except (aiohttp.ContentTypeError, KeyError):
                        data = None
                        message = response.reason

                    raise graphql.client.ClientResponseHTTPError(message, response, data)

                # NOTE: While the GraphQL specification does not mandate a
                #       serialization format, JSON is by far the most
                #       common response serialization for GraphQL servers.

                data = await response.json()
        except aiohttp.ClientResponseError as e:
            raise graphql.client.ClientResponseError(e.message) from e
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

                    exceptions.append(
                        graphql.client.ClientResponseGraphQLError(message, response, data)
                    )

                if False:  # len(exceptions) > 1:
                    # TODO: I'm not sure I love this interface.
                    raise ClientResponseGraphQLErrorCollection(exceptions)
                else:
                    raise exceptions[0]

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
