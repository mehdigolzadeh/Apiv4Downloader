import datetime
import typing

from github import utils
from github.abc import Actor
from github.abc import Node
from github.abc import ProfileOwner
from github.abc import ProjectOwner
from github.abc import RepositoryOwner
from github.abc import Type
from github.abc import UniformResourceLocatable
from .commitcomment import CommitComment


class User(Actor, Node, ProfileOwner, ProjectOwner, RepositoryOwner, Type,
           UniformResourceLocatable):
    """
    Represents a GitHub user account.

    https://developer.github.com/v4/object/user/

    Implements:

    * :class:`~abc.Actor`
    * :class:`~abc.Node`
    * :class:`~abc.ProfileOwner`
    * :class:`~abc.ProjectOwner`
    * :class:`~abc.RepositoryOwner`
    * :class:`~abc.Type`
    * :class:`~abc.UniformResourceLocatable`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self) :
        return "<{0.__class__.__name__} login='{0.login}'>".format(self)

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(user, http) for user in data]

    @property
    def bio(self) :
        """
        The user's public profile bio.
        """

        return self.data["bio"] or ""

    @property
    def company(self):
        """
        The user's public profile company.
        """

        return self.data["company"]
    
    @property
    def created_at(self):
        """
        The date and time the user was created.
        """

        return utils.iso_to_datetime(self.data["createdAt"])

    @property
    def database_id(self) :
        """
        The user's primary key from the database.
        """

        return self.data["databaseId"]

    @property
    def is_bounty_hunter(self) :
        """
        Whether the user is a participant in the GitHub Security Bug Bounty.
        """

        return self.data["isBountyHunter"]

    @property
    def is_campus_expert(self) :
        """
        Whether the user is a participant in the GitHub Campus Experts Program.
        """

        return self.data["isCampusExpert"]

    @property
    def is_developer_program_member(self) :
        """
        Whether the user is a GitHub Developer Program member.
        """

        return self.data["isDeveloperProgramMember"]

    @property
    def is_employee(self) :
        """
        Whether the user is a GitHub employee.
        """

        return self.data["isEmployee"]

    @property
    def is_hireable(self) :
        """
        Whether the user has marked themselves as for hire.
        """

        return self.data["isHireable"]

    @property
    def is_site_administrator(self) :
        """
        Whether the user is a site administrator.
        """

        return self.data["isSiteAdmin"]

    @property
    def is_viewer(self) :
        """
        Whether or not the user is the viewing user.
        """

        return self.data["isViewer"]
    
    @property
    def updated_at(self):
        """
        The date and time the user was last updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)

    def fetch_commit_comments(self):
        """
        Fetches the user's commit comments.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The user does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.CommitComment`]
            A list of commit comments created by the user.
        """

        data = self.http.fetch_user_commit_comments(self.id)
        return CommitComment.from_data(data, self.http)

class AuthenticatedUser(User):
    """
    Represents the authenticated GitHub user account, "viewer".

    https://developer.github.com/v4/object/user/

    Implements:

    * :class:`~abc.Actor`
    * :class:`~abc.Node`
    * :class:`~abc.ProfileOwner`
    * :class:`~abc.ProjectOwner`
    * :class:`~abc.RepositoryOwner`
    * :class:`~abc.Type`
    * :class:`~abc.UniformResourceLocatable`
    """

    @classmethod
    def from_data(cls, data, http):
        return cls(data, http)
