import typing

from github.abc import Assignable
from github.abc import Closable
from github.abc import Comment
from github.abc import Commentable
from github.abc import Labelable
from github.abc import Lockable
from github.abc import Node
from github.abc import Participable
from github.abc import Reactable
from github.abc import RepositoryNode
from github.abc import Subscribable
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.abc import Updatable
from github.enums import IssueState


class Issue(Assignable, Closable, Comment, Commentable, Labelable, Lockable, Node, Participable,
            Reactable, RepositoryNode, Subscribable, Type, UniformResourceLocatable, Updatable):
    
    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(issue, http) for issue in data]

    @property
    def database_id(self):
        """
        The primary key for the issue from the database.
        """

        return self.data["databaseId"]

    @property
    def number(self):
        """
        The issue number.
        """

        return self.data["number"]

    @property
    def state(self):
        """
        The issue state.
        """

        state = self.data["state"]
        return IssueState.from_data(state)

    @property
    def title(self):
        """
        The issue title.
        """

        return self.data["title"]
