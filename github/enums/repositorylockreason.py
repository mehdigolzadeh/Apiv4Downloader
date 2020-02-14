class RepositoryLockReason():
    """
    Represents the reason for a given repository to be in a locked state.

    https://developer.github.com/v4/enum/repositorylockreason/
    """

    __slots__ = ("_lock_reason",)

    def __init__(self, lock_reason):
        self._lock_reason = lock_reason

    def __repr__(self):
        return "<{0.__class__.__name__} '{0._lock_reason}'>".format(self)

    @classmethod
    def from_data(cls, lock_reason):
        return cls(lock_reason)

    @property
    def billing(self):
        """
        The repository is locked for a billing-related reason.
        """

        return self._lock_reason == "BILLING"

    @property
    def migrating(self):
        """
        The repository is locked due to a migration.
        """

        return self._lock_reason == "MIGRATING"

    @property
    def moving(self):
        """
        The repository is locked due to a move.
        """

        return self._lock_reason == "MOVING"

    @property
    def rename(self):
        """
        The repository is locked due to a rename.
        """

        return self._lock_reason == "RENAME"
