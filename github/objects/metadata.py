import typing

from github.abc import Type


class Metadata(Type):
    """
    Represents information about the GitHub instance.

    https://developer.github.com/v4/object/githubmetadata/

    Implements:

    * :class:`~abc.Type`
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_data(cls, data):
        return cls(data)

    @property
    def git_ip_addresses(self):
        """
        IP addresses that users connect to for git operations.
        """

        return self.data["gitIpAddresses"]

    @property
    def github_services_sha(self):
        """
        SHA of github-services.
        """

        return self.data["gitHubServicesSha"]

    @property
    def hook_ip_addresses(self) :
        """
        IP addresses that service hooks are sent from.
        """

        return self.data["hookIpAddresses"]

    @property
    def importer_ip_addresses(self) :
        """
        IP addresses that the importer connects from.
        """

        return self.data["importerIpAddresses"]

    @property
    def is_authentication_verifiable(self) :
        """
        Whether or not users are verified.
        """

        return self.data["isPasswordAuthenticationVerifiable"]

    @property
    def pages_ip_addresses(self) :
        """
        IP addresses for GitHub Pages' A records.
        """

        return self.data["pagesIpAddresses"]
