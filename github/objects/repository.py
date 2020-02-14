import datetime
import typing

from github import utils
from github.abc import Node
from github.abc import ProjectOwner
from github.abc import Subscribable
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.enums import RepositoryLockReason
from github.enums import RepositoryPermissions
from .codeofconduct import CodeOfConduct
from .language import Language
from .license import License
from .organization import Organization
from .user import User


class Repository(Node, ProjectOwner, Subscribable, Type, UniformResourceLocatable):
    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self) :
        return "<{0.__class__.__name__} owner='{0.owner.login}' name='{0.name}'>".format(self)

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(repository, http) for repository in data]

    @property
    def allows_merge_commit(self):
        return self.data["mergeCommitAllowed"]

    @property
    def allows_rebase_merge(self):
        return self.data["rebaseMergeAllowed"]

    @property
    def allows_squash_merge(self):
        return self.data["squashMergeAllowed"]

    @property
    def created_at(self):
        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self):
        """
        The primary key for the repository from the database.
        """

        return self.data["databaseId"]

    @property
    def default_branch(self):
        """
        The name of the default branch.
        """

        return self.data["defaultBranchRef"]["name"]

    @property
    def description(self):
        """
        The description of the repository.
        """

        return self.data["description"] or ""

    @property
    def disk_usage(self):
        """
        The number of kilobytes the repository occupies on disk.
        """

        return self.data["diskUsage"]

    @property
    def fork_count(self):
        """
        The number of forks created from the repository.
        """

        return self.data["forkCount"]

    @property
    def has_issues(self):
        """
        Whether or not the repository has issues enabled.
        """

        return self.data["hasIssuesEnabled"]

    @property
    def has_wiki(self):
        """
        Whether or not the repository has wiki enabled.
        """

        return self.data["hasWikiEnabled"]

    @property
    def is_archived(self):
        """
        Whether or not the repository is archived.
        """

        return self.data["isArchived"]

    @property
    def is_disabled(self):
        """
        Whether or not the repository is disabled.
        """

        return self.data["isDisabled"]

    @property
    def is_fork(self):
        """
        Whether or not the repository is a fork of another repository.
        """

        return self.data["isFork"]

    @property
    def is_locked(self):
        """
        Whether or not the repository is locked.
        """

        return self.data["isLocked"]

    @property
    def is_mirror(self):
        """
        Whether or not the repository is a mirror of another repository.
        """

        return self.data["isMirror"]

    @property
    def is_private(self):
        """
        Whether or not the repository is private.
        """

        return self.data["isPrivate"]

    @property
    def is_template(self):
        """
        Whether or not the repository is a template repository.
        """

        return self.data["isTemplate"]

    
    @property
    def lock_reason(self):
        """
        The reason for the repository to be in a locked state.
        """

        lock_reason = self.data["lockReason"]
        if lock_reason:
            return RepositoryLockReason.from_data(lock_reason)

    @property
    def name(self) :
        """
        The name of the repository.
        """

        return self.data["name"]

    @property
    def owner(self):
        """
        The owner of the repository.
        """

        owner = self.data["owner"]
        
        if owner["__typename"] == "Organization":
            return Organization.from_data(owner, self.http)
        elif owner["__typename"] == "User":
            return User.from_data(owner, self.http)

    @property
    def parent(self):
        """
        The repository's parent repository.
        """

        parent = self.data["parent"]
        if not parent:
            return None

        parent["parent"] = None
        parent["templateRepository"] = None

        return PartialRepository.from_data(parent, self.http)

    @property
    def primary_language(self):
        """
        The primary language of the repository.
        """

        primary_language = self.data["primaryLanguage"]
        if primary_language:
            return Language.from_data(primary_language)

    @property
    def pushed_at(self):
        """
        The date and time when the repository was last pushed to.
        """

        pushed_at = self.data["pushedAt"]
        if pushed_at:
            return utils.iso_to_datetime(pushed_at)

    @property
    def template(self):
        """
        The repository's template repository.
        """

        template = self.data["templateRepository"]
        if not template:
            return None

        template["parent"] = None
        template["templateRepository"] = None

        return PartialRepository.from_data(template, self.http)

    @property
    def updated_at(self):
        """
        The date and time when the repository was last updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)

    @property
    def viewer_can_administer(self) :
        """
        Whether or not the authenticated user can administer the repository.
        """

        return self.data["viewerCanAdminister"]

    @property
    def viewer_can_update_topics(self) :
        """
        Whether or not the authenticated user can update topics in the repository.
        """

        return self.data["viewerCanUpdateTopics"]

    @property
    def viewer_permissions(self):
        """
        The authenticated user's permissions in the repository.
        """

        permissions = self.data["viewerPermission"]
        return RepositoryPermissions.from_data(permissions)

    def fetch_assignable_users(self):
        """
        Fetches a list of users that can be assigned to issues in the repository.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The repository does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.User`]
            A list of users that can be assigned to issues in the repository.
        """

        data = self.http.fetch_repository_assignable_users(self.id)
        return User.from_data(data, self.http)

    def fetch_collaborators(self):
        """
        Fetches a list of collaborators associated with the repository.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The repository does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.User`]
            A list of collaborators associated with the repository.
        """

        data = self.http.fetch_repository_collaborators(self.id)
        return User.from_data(data, self.http)

class PartialRepository(Repository):
    """
    Represents a GitHub repository.

    https://developer.github.com/v4/object/repository/

    Implements:

    * :class:`~abc.Node`
    * :class:`~abc.ProjectOwner`
    * :class:`~abc.Subscribable`
    * :class:`~abc.Type`
    * :class:`~abc.UniformResourceLocatable`

    Using this partial-class will result in the following attributes being ``None`` at all times:

    * :attr:`~github.Repository.parent`
    * :attr:`~github.Repository.template`
    """

    __slots__ = ("data", "http")
