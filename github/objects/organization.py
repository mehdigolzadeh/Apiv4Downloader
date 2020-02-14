import typing

from github.abc import Actor
from github.abc import Node
from github.abc import ProfileOwner
from github.abc import ProjectOwner
from github.abc import RepositoryOwner
from github.abc import Type
from github.abc import UniformResourceLocatable


class Organization(Actor, Node, ProfileOwner, ProjectOwner, RepositoryOwner, Type,
                   UniformResourceLocatable):
    """
    Represents a GitHub organization.

    https://developer.github.com/v4/object/organization/

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
            return [cls(organization, http) for organization in data]

    @property
    def database_id(self) :
        """
        The organization's primary key from the database.
        """

        return self.data["databaseId"]

    @property
    def description(self) :
        """
        The organization's description.
        """

        return self.data["description"] or ""

    @property
    def is_verified(self) :
        """
        Whether or not the organization's public email is verified.
        """

        return self.data["isVerified"]

    @property
    def new_team_resource_path(self) :
        """
        The organization's new team resource path.
        """

        return self.data["newTeamResourcePath"]

    @property
    def new_team_url(self) :
        """
        The organization's new team url.
        """

        return self.data["newTeamUrl"]

    @property
    def teams_resource_path(self) :
        """
        The organization's teams resource path.
        """

        return self.data["teamsResourcePath"]

    @property
    def teams_url(self) :
        """
        The organization's teams url.
        """

        return self.data["teamsUrl"]

    @property
    def viewer_can_administer(self) :
        """
        Whether or not the authenticated user can administer the organization.
        """

        return self.data["viewerCanAdminister"]

    @property
    def viewer_can_create_repositories(self) :
        """
        Whether or not the authenticated user can create repositories in the organization.
        """

        return self.data["viewerCanCreateRepositories"]

    @property
    def viewer_can_create_teams(self) :
        """
        Whether or not the authenticated user can create teams in the organization.
        """

        return self.data["viewerCanCreateTeams"]

    @property
    def viewer_is_member(self) :
        """
        Whether or not the authenticated user is a member of the organization.
        """

        return self.data["viewerIsAMember"]
