from __future__ import annotations
from typing import NamedTuple

from graphql import client


class _VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    release: str
    serial: int


version: str = "0.1.0a"
version_info: _VersionInfo = _VersionInfo(0, 1, 0, "alpha", 0)


__all__ = []
