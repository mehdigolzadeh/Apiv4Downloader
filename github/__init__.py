import collections

from github import abc
from github import enums
from github import query
from github.objects import *
from github.apiv4 import GitHub
from github.githttp import HTTPClient


__version__ = "0.5.0"

VersionInfo = collections.namedtuple("VersionInfo", "major minor micro releaselevel serial")
version_info = VersionInfo(major=0, minor=5, micro=0, releaselevel="final", serial=0)
