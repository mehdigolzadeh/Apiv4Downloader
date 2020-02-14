class Actor():
    """
    Represents an object which can take actions on GitHub.

    https://developer.github.com/v4/interface/actor/

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Bot`
    * :class:`~github.Mannequin`
    * :class:`~github.Organization`
    * :class:`~github.User`
    """

    __slots__ = ()

    @property
    def avatar_url(self):
        """
        A url pointing to the actor's public avatar.
        """

        return self.data["avatarUrl"]

    @property
    def identicon_url(self):
        """
        A url pointing to the actor's identicon.
        """

        return "https://identicons.github.com/{0}.png".format(self.data["login"])

    @property
    def login(self):
        """
        The actor's username.
        """

        return self.data["login"]

    def fetch_avatar_url(self, *, size: int=None):
        """
        |coro|

        Fetches a url pointing to the actor's avatar.

        Parameters
        ----------
        size: Optional[:class:`int`]
            The size of the avatar.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The actor does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`str`
            The url pointing to the actor's avatar.
        """
        
        avatar_url = self.http.fetch_actor_avatar_url(self.id, size)
        return avatar_url
