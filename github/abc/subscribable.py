
from github.enums import RepositorySubscription as SubscriptionState


class Subscribable():
    """
    Represents an object which can be subscribed to.

    https://developer.github.com/v4/interface/subscribable/

    Implemented by:
    
    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    * :class:`~github.Repository`
    """

    __slots__ = ()

    @property
    def viewer_can_subscribe(self):
        """
        Whether or not the authenticated user can subscribe to the subscribable.
        """

        return self.data["viewerCanSubscribe"]

    @property
    def viewer_subscription(self):
        """
        The authenticated user's subscription state to the subscribable.
        """

        subscription = self.data["viewerSubscription"]
        return SubscriptionState.from_data(subscription)

    def ignore(self):
        """
        |coro|

        Updates the authenticated user's subscription state to "IGNORED".

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The subscribable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        self.http.update_subscription(self.id, "IGNORED")
        
    def subscribe(self):
        """
        |coro|

        Updates the authenticated user's subscription state to "SUBSCRIBED".

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The subscribable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        self.http.update_subscription(self.id, "SUBSCRIBED")

    def unsubscribe(self):
        """
        |coro|

        Updates the authenticated user's subscription state to "UNSUBSCRIBED".

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The subscribable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        self.http.update_subscription(self.id, "UNSUBSCRIBED")
