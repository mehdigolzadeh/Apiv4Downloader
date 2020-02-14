import typing

from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable


class CodeOfConduct(Node, Type, UniformResourceLocatable):
    """
    Represents a Code of Conduct.

    https://developer.github.com/v4/object/codeofconduct

    Implements:

    * :class:`~abc.Node`
    * :class:`~abc.Type`
    * :class:`~abc.UniformResourceLocatable`
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<{0.__class__.__name__} key='{0.key}'>".format(self)

    @classmethod
    def from_data(cls, data):
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
           return [cls(code) for code in data]

    @property
    def body(self):
        """
        The body of the Code of Conduct.
        """

        return self.data["body"]

    @property
    def key(self):
        """
        The key of the Code of Conduct.
        """

        return self.data["key"]

    @property
    def name(self):
        """
        The name of the Code of Conduct.
        """

        return self.data["name"]
