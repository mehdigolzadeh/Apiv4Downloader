import typing

from github.enums import LockReason


class Lockable():
    """
    Represents an object which can be locked.

    https://developer.github.com/v4/interface/lockable/

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    @property
    def is_locked(self):
        """
        Whether or not the lockable is locked.
        """

        return self.data["locked"]

    @property
    def lock_reason(self):
        """
        The reason for the lockable being locked.
        """

        reason = self.data["activeLockReason"]
        if reason:
            return LockReason.from_data(reason)

    def lock(self, *, reason: str=None):
        """
        |coro|

        Locks the lockable.

        Parameters
        ----------
        reason: Optional[:class:`str`]
            The reason for locking the lockable. Can be one of
            ``"OFF_TOPIC"``, ``"RESOLVED"``, ``"SPAM"``,
            ``"TOO_HEATED"``.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to lock the lockable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The lockable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        self.http.lock(self.id, reason)

    def unlock(self):
        """
        |coro|

        Unlocks the lockable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to unlock the lockable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The lockable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        self.http.unlock(self.id)

