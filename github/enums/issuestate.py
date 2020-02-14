class IssueState():
    """
    Represents the state of an issue.

    https://developer.github.com/v4/enum/issuestate/
    """

    __slots__ = ("_state",)

    def __init__(self, state):
        self._state = state

    def __repr__(self):
        return "<{0.__class__.__name__} '{0._state}'>".format(self)

    @classmethod
    def from_data(cls, state):
        return cls(state)

    @property
    def closed(self):
        """
        The issue is closed.
        """

        return self._state == "CLOSED"

    @property
    def open(self):
        """
        The issue is open.
        """

        return self._state == "OPEN"
