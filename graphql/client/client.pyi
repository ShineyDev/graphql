from aiohttp import ClientSession


class Client:
    def __init__(self, *, session: ClientSession, url: str) -> None: ...

    async def request(self, document: str, operation: str=..., **variables) -> dict: ...
