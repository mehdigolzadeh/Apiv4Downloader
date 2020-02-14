import typing

from github.abc import Node
from github.abc import Type
from .licenserule import LicenseRule


class License(Node, Type):
    """
    A repository's source license.

    https://developer.github.com/v4/object/license/

    Implements:

    * :class:`~abc.Node`
    * :class:`~abc.Type`
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
            return [cls(license) for license in data]

    @property
    def body(self):
        """
        The full text of the license.
        """

        return self.data["body"]

    @property
    def conditions(self):
        """
        The conditions set by the license.
        """

        conditions = self.data["conditions"]
        return LicenseRule.from_data(conditions)

    @property
    def description(self):
        """
        A human-readable description of the license.
        """

        return self.data["description"]

    @property
    def implementation(self):
        """
        Instructions on how to implement the license.
        """

        return self.data["implementation"]

    @property
    def is_featured(self):
        """
        Whether the license is featured.
        """

        return self.data["featured"]

    @property
    def is_hidden(self):
        """
        Whether the license is not displayed in license pickers.
        """

        return self.data["hidden"]

    @property
    def is_pseudo(self):
        """
        Whether the license is a pseudo-license placeholder.
        """

        return self.data["pseudoLicense"]

    @property
    def key(self):
        """
        The lowercased SPDX ID of the license.
        """

        return self.data["key"]

    @property
    def limitations(self):
        """
        The limitations set by the license.
        """

        limitations = self.data["limitations"]
        return LicenseRule.from_data(limitations)

    @property
    def name(self):
        """
        The full name of the license specified by |spdx|.
        """

        return self.data["name"]

    @property
    def nickname(self):
        """
        The customary short name of the license.
        """

        return self.data["nickname"]

    @property
    def permissions(self):
        """
        The permissions set by the license.
        """

        permissions = self.data["permissions"]
        return LicenseRule.from_data(permissions)

    @property
    def spdx_id(self):
        """
        The short identifier of the license specified by |spdx|.
        """

        return self.data["spdxId"]

    @property
    def url(self):
        """
        The url to the license on |choosealicense|.
        """

        return self.data["url"]
