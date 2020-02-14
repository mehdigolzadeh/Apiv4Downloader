class PullRequestState():
    """
    Represents the state of a pull request.

    https://developer.github.com/v4/enum/pullrequeststate/
    """

    __slots__ = ("_state",)

    def __init__(self, state):
        self._state = state

    def __repr__(self) :
        return "<{0.__class__.__name__} '{0._state}'>".format(self)

    @classmethod
    def from_data(cls, state):
        return cls(state)

    @property
    def closed(self):
        """
        The pull request is closed.
        """

        return self._state == "CLOSED"

    @property
    def merged(self):
        """
        The pull request is merged.
        """

        return self._state == "MERGED"

    @property
    def open(self):
        """
        The pull request is open.
        """

        return self._state == "OPEN"
