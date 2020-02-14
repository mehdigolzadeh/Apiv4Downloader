import typing


class CannotUpdateReason():
    """
    Represents a reason the authenticated user cannot update a comment.

    https://developer.github.com/v4/enum/commentcannotupdatereason/
    """

    __slots__ = ("data",)

    def __init__(self, reason):
        self._reason = reason

    def __repr__(self):
        return "<{0.__class__.__name__} '{0._reason}'>".format(self)

    @classmethod
    def from_data(cls, data):
        reasons = list()

        for (reason) in data:
            reasons.append(cls(reason))

        return reasons

    @property
    def archived(self):
        """
        You cannot update this comment because the repository is archived.
        """

        return self._reason == "ARCHIVED"

    @property
    def denied(self):
        """
        You cannot update this comment.
        """

        return self._reason == "DENIED"

    @property
    def insufficient_access(self):
        """
        You must be the author or have write access to update this comment.
        """

        return self._reason == "INSUFFICIENT_ACCESS"

    @property
    def locked(self):
        """
        You cannot update this comment because the issue is locked.
        """

        return self._reason == "LOCKED"

    @property
    def maintenance(self):
        """
        You cannot update this comment because the repository is under maintenance.
        """

        return self._reason == "MAINTENANCE"

    @property
    def login_required(self):
        """
        You must be logged in to update this comment.
        """

        return self._reason == "LOGIN_REQUIRED"

    @property
    def verified_email_required(self):
        """
        At least one email address must be verified to update this comment.
        """

        return self._reason == "VERIFIED_EMAIL_REQUIRED"
    