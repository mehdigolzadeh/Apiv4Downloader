import typing


class Labelable():
    """
    Represents an object which can be labeled.

    https://developer.github.com/v4/interface/labelable/

    Implemented by:

    * :class:`github.Issue`
    * :class:`github.PullRequest`
    """

    __slots__ = ()

    def fetch_labels(self):
        """
        |coro|

        Fetches a list of labels from the labelable.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The labelable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        # prevent cyclic imports
        from github.objects import Label

        data = self.http.fetch_labelable_labels(self.id)
        return Label.from_data(data, self.http)
        
    def add_labels(self, *labels: "Label"):
        """
        |coro|

        Adds labels to the labelable.

        Parameters
        ----------
        \\*labels: Iterable[:class:`github.Label`]
            An iterable of labels.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to add labels to the labelable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The labelable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        labels = [label.id for label in labels]
        self.http.add_labels(self.id, labels)

    def clear_labels(self):
        """
        |coro|

        Clears all labels from the labelable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to clear labels from the labelable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The labelable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        self.http.clear_labels(self.id)

    def remove_labels(self, *labels: "Label"):
        """
        |coro|

        Removes labels from the labelable.

        Parameters
        ----------
        \\*labels: Iterable[:class:`github.Label`]
            An iterable of labels.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to remove labels from the labelable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The labelable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        labels = [label.id for label in labels]
        self.http.remove_labels(self.id, labels)
