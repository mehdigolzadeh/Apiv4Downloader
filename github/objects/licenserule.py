import typing

from github.abc import Type


class LicenseRule(Type):
    """
    Represents a license's conditions, permissions, or limitations.

    https://developer.github.com/v4/object/licenserule/

    Implements:

    * :class:`~abc.Type`
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<{0.__class__.__name__} key='{0.key}'>".format(self)

    @classmethod
    def from_data(cls, data):
        return [cls(rule) for rule in data]
    
    @property
    def description(self):
        """
        A description of the rule.
        """

        return self.data["description"]

    @property
    def key(self):
        """
        The machine-readable rule key.
        """

        return self.data["key"]

    @property
    def label(self):
        """
        The human-readable rule label.
        """

        return self.data["label"]
