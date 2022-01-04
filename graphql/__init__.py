import collections

from graphql import client as client


__all__ = []


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "0.1.0a"
version_info = _VersionInfo(0, 1, 0, "alpha", 0)
