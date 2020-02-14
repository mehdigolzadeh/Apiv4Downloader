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
from github.enums import PullRequestState


class PullRequest(Assignable, Closable, Comment, Commentable, Labelable, Lockable, Node,
                  Participable, Reactable, RepositoryNode, Subscribable, Type,
                  UniformResourceLocatable, Updatable):
    """
    Represents a pull request on a :class:`~github.Repository`.

    https://developer.github.com/v4/object/pullrequest/

    Implements:

    * :class:`~abc.Assignable`
    * :class:`~abc.Closable`
    * :class:`~abc.Comment`
    * :class:`~abc.Commentable`
    * :class:`~abc.Labelable`
    * :class:`~abc.Lockable`
    * :class:`~abc.Node`
    * :class:`~abc.Participable`
    * :class:`~abc.Reactable`
    * :class:`~abc.RepositoryNode`
    * :class:`~abc.Subscribable`
    * :class:`~abc.Type`
    * :class:`~abc.UniformResourceLocatable`
    * :class:`~abc.Updatable`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(pull, http) for pull in data]

    @property
    def additions(self) :
        """
        The number of additions in the pull request.
        """

        return self.data["additions"]

    @property
    def database_id(self) :
        """
        The primary key for the pull request from the database.
        """

        return self.data["databaseId"]

    @property
    def deletions(self) :
        """
        The number of deletions in the pull request.
        """

        return self.data["deletions"]

    @property
    def number(self) :
        """
        The pull request number.
        """

        return self.data["number"]

    @property
    def state(self):
        """
        The pull request state.
        """

        state = self.data["state"]
        return PullRequestState.from_data(state)

    @property
    def title(self) :
        """
        The pull request title.
        """

        return self.data["title"]
