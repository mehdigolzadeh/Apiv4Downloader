import typing

class Participable():
    """
    Represents an object which can be participated in.

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    def fetch_participants(self):
        """
        |coro|

        Fetches a list of users participating on the participable.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The participable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.User`]
            A list of users participating on the participable.
        """

        from github.objects import User

        if self.data["__typename"] == "Issue":
            data = self.http.fetch_issue_participants(self.id)
        elif self.data["__typename"] == "PullRequest":
            data = self.http.fetch_pull_request_participants(self.id)

        return User.from_data(data, self.http)
