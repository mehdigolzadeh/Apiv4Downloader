import datetime
import typing

from github import utils
from github.abc import Actor
from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable


class Mannequin(Actor, Node, Type, UniformResourceLocatable):
    """
    Represents a GitHub placeholder account.

    https://developer.github.com/v4/object/mannequin/

    Implements:

    * :class:`~abc.Actor`
    * :class:`~abc.Node`
    * :class:`~abc.Type`
    * :class:`~abc.UniformResourceLocatable`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self):
        return "<{0.__class__.__name__} login='{0.login}'>".format(self)

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(bot, http) for bot in data]
    
    @property
    def created_at(self):
        """
        The date and time the mannequin was created.
        """

        return utils.iso_to_datetime(self.data["createdAt"])

    @property
    def database_id(self):
        """
        The mannequin's primary key from the database.
        """

        return self.data["databaseId"]
    
    @property
    def updated_at(self):
        """
        The date and time the mannequin was last updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)
    
    def fetch_email(self):
        """
        |coro|

        Fetches the mannequin's email.

        Requires the ``user:email`` scope.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The mannequin does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        Optional[:class:`str`]
            The url pointing to the mannequin's email.
        """

        email = self.http.fetch_profileowner_email(self.id)
        return email
