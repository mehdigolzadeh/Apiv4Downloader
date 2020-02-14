
import typing


class ProfileOwner():
    """
    Represents the owner of a GitHub profile.

    https://developer.github.com/v4/interface/profileowner/

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Organization`
    * :class:`~github.User`
    """

    __slots__ = ()

    @property
    def has_pinnable_items(self) :
        """
        Whether or not the profile owner has any items that can be pinned to the profile.
        """

        return self.data["anyPinnableItems"]

    @property
    def location(self):
        """
        The profile owner's location.
        """

        return self.data["location"]

    @property
    def name(self):
        """
        The profile owner's name.
        """

        return self.data["name"]

    @property
    def pinned_items_remaining(self):
        """
        The number of items the profile owner can pin to the profile.
        """

        return self.data["pinnedItemsRemaining"]

    @property
    def viewer_can_change_pinned_items(self) :
        """
        Whether or not the authenticated user can change the pinned items on the profile.
        """

        return self.data["viewerCanCreateProjects"]

    @property
    def website(self):
        """
        The profile owner's website.
        """

        return self.data["websiteUrl"]
    
    def fetch_email(self):
        """
        |coro|

        Fetches the profile owner's email.

        Requires the ``user:email`` scope.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The profile owner does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        Optional[:class:`str`]
            The profile owner's email.
        """

        email = self.http.fetch_profileowner_email(self.id)
        return email
