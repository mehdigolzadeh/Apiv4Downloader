class RepositorySubscription():
    """
    Represents a user's subscription state.

    https://developer.github.com/v4/enum/subscriptionstate/
    """

    __slots__ = ("_subscription",)

    def __init__(self, subscription):
        self._subscription = subscription

    def __repr__(self):
        return "<{0.__class__.__name__} '{0._subscription}'>".format(self)

    @classmethod
    def from_data(cls, subscription):
        return cls(subscription)

    @property
    def ignored(self):
        """
        The user is never notified.
        """

        return self._subscription == "IGNORED"

    @property
    def subscribed(self):
        """
        The user is notified of all conversations.
        """

        return self._subscription == "SUBSCRIBED"

    @property
    def unsubscribed(self):
        """
        The user is only notified when participating or mentioned.
        """

        return self._subscription == "UNSUBSCRIBED"
