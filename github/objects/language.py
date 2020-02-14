from github import utils
from github.abc import Node
from github.abc import Type


class Language(Node, Type):
    """
    Represents a programming language found in repositories.

    https://developer.github.com/v4/object/language/

    Implements:

    * :class:`~abc.Node`
    * :class:`~abc.Type`
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<{0.__class__.__name__} name='{0.name}'>".format(self)

    @classmethod
    def from_data(cls, data):
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            return [cls(language) for language in data]

    @property
    def color(self):
        """
        The color of the language in the GitHub UI.
        """

        return self.data["color"]

    @property
    def colour(self):
        """
        An alias for :attr:`~Language.color`.
        """

        return self.color

    @property
    def name(self):
        """
        The name of the language.
        """

        return self.data["name"]
