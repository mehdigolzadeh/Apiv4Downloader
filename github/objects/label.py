import datetime
import typing

from github import utils
from github.abc import Node
from github.abc import RepositoryNode
from github.abc import Type
from github.abc import UniformResourceLocatable
from .issue import Issue
from .pullrequest import PullRequest


class Label(Node, RepositoryNode, Type, UniformResourceLocatable):
    """
    Represents a label on a :class:`~abc.Labelable`.

    https://developer.github.com/v4/object/label/

    Implements:

    * :class:`~abc.Node`
    * :class:`~abc.RepositoryNode`
    * :class:`~abc.Type`
    * :class:`~abc.UniformResourceLocatable`
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
            return [cls(label, http) for label in data]

    @property
    def color(self):
        """
        The color of the label in the GitHub UI.
        """

        return self.data["color"]

    @property
    def colour(self):
        """
        An alias for :attr:`~github.Label.color`.
        """

        return self.data["color"]

    @property
    def created_at(self):
        """
        The date and time at which the label was created.
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def description(self):
        """
        The description of the label.
        """

        return self.data["description"] or ""

    @property
    def is_default(self):
        """
        Whether or not the label is a default label.
        """

        return self.data["isDefault"]

    @property
    def name(self):
        """
        The name of the label.
        """

        return self.data["name"]

    @property
    def updated_at(self):
        """
        The date and time at which the label was updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)

    def fetch_issues(self):
        """
        Fetches a list of issues with the label.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The label does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.Issue`]
            A list of issues with the label.
        """

        data = self.http.fetch_label_issues(self.id)
        return Issue.from_data(data, self.http)

    def fetch_pull_requests(self):
        """
        Fetches a list of pull requests with the label.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The label does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.PullRequest`]
            A list of pull requests with the label.
        """

        data = self.http.fetch_label_pull_requests(self.id)
        return PullRequest.from_data(data, self.http)
