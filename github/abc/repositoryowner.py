class RepositoryOwner():
    """
    Represents the owner of a GitHub repository.

    https://developer.github.com/v4/interface/repositoryowner/

    Implemented by:

    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Organization`
    * :class:`~github.User`
    """

    __slots__ = ()

    def fetch_repository(self, name: str):
        """
        |coro|

        Fetches a repository from the repository owner.

        Parameters
        ----------
        name: :class:`str`
            The repository name.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The repository does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`github.Repository`
            The repository.
        """

        # prevent cyclic imports
        from github.objects import Repository

        data = self.http.fetch_repository(self.login, name)
        return Repository.from_data(data, self.http)
