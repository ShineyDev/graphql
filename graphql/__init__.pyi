from typing import NamedTuple

from graphql import client


class _VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
