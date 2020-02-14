from github.abc import Comment
from github.abc import Deletable
from github.abc import Node
from github.abc import Reactable
from github.abc import RepositoryNode
from github.abc import Type
from github.abc import Updatable


class CommitComment(Comment, Deletable, Node, Reactable, RepositoryNode, Type, Updatable):
    """
    Represents a comment on a :class:`~github.Commit`.

    https://developer.github.com/v4/object/commitcomment/

    Implements:

    * :class:`~abc.Comment`
    * :class:`~abc.Deletable`
    * :class:`~abc.Node`
    * :class:`~abc.Reactable`
    * :class:`~abc.RepositoryNode`
    * :class:`~abc.Type`
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
            return [cls(comment, http) for comment in data]
