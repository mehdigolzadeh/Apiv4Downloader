class LockReason():
    """
    Represents the reason for a lockable to be in a locked state.

    https://developer.github.com/v4/enum/lockreason/
    """

    __slots__ = ("_reason",)

    def __init__(self, reason):
        self._reason = reason

    def __repr__(self):
        return "<{0.__class__.__name__} '{0._reason}'>".format(self)

    @classmethod
    def from_data(cls, reason):
        return cls(reason)

    @property
    def off_topic(self):
        """
        The lockable is locked because the conversation was off-topic.
        """

        return self._reason == "OFF_TOPIC"

    @property
    def resolved(self):
        """
        The lockable is locked because the conversation was resolved.
        """

        return self._reason == "RESOLVED"

    @property
    def spam(self):
        """
        The lockable is locked because the conversation was spam.
        """

        return self._reason == "SPAM"

    @property
    def too_heated(self):
        """
        The lockable is locked because the conversation was too heated.
        """

        return self._reason == "TOO_HEATED"
