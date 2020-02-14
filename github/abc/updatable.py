import typing

from github.enums import CannotUpdateReason


class Updatable():
    """
    Represents an object which can be updated.

    https://developer.github.com/v4/interface/updatable/

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    @property
    def viewer_can_update(self):
        """
        Whether or not the authenticated user can update the updatable.
        """

        return self.data["viewerCanUpdate"]

    @property
    def viewer_cannot_update_reasons(self):
        """
        A list of reasons why the authenticated user cannot update this updatable.
        """

        reasons = self.data["viewerCannotUpdateReasons"]
        return CannotUpdateReason.from_data(reasons)

    def update(self, **kwargs):
        """
        |coro|

        Updates the updatable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to update the updatable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The updatable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        ...
