import typing


class Commentable():
    """
    Represents an object which can be commented on.

    Implemented by:

    * :class:`github.Issue`
    * :class:`github.PullRequest`
    """

    __slots__ = ()

    def fetch_comments(self):
        """
        |coro|

        Fetches a list of comments on the commentable.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The commentable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[Union[:class:`~github.CommitComment`, \
                   :class:`~github.GistComment`, \
                   :class:`~github.IssueComment`, \
                   :class:`~github.PullRequestComment`, \
                   :class:`~github.PullRequestReviewComment`]]
            A list of issues with the label
        """

        # prevent cyclic imports
        from github.objects import CommitComment
        #from github.objects import GistComment
        #from github.objects import IssueComment
        #from github.objects import PullRequestComment
        #from github.objects import PullRequestReview
        #from github.objects import PullRequestReviewComment

        data = self.http.fetch_commentable_comments(self.id)

        if data[0]["__typename"] == "CommitComment":
            return CommitComment.from_data(data, self.http)
        elif data[0]["__typename"] == "GistComment":
            return GistComment.from_data(data, self.http)
        elif data[0]["__typename"] == "IssueComment":
            if self.data["__typename"] == "Issue":
                return IssueComment.from_data(data, self.http)
            elif self.data["__typename"] == "PullRequest":
                return PullRequestComment.from_data(data, self.http)
        elif data[0]["__typename"] == "PullRequestReviewComment":
            return PullRequestReviewComment.from_data(data, self.http)

    def add_comment(self, body: str) :
        """
        |coro|

        Adds a comment to the commentable.

        Parameters
        ----------
        body: :class:`str`
            The body of the comment.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to comment on the commentable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The commentable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        Union[:class:`~github.CommitComment`, \
              :class:`~github.GistComment`, \
              :class:`~github.IssueComment`, \
              :class:`~github.PullRequestComment`, \
              :class:`~github.PullRequestReviewComment`]
            The added comment.
        """
        
        # prevent cyclic imports
        from github.objects import CommitComment
        #from github.objects import GistComment
        #from github.objects import IssueComment
        #from github.objects import PullRequestComment
        #from github.objects import PullRequestReview
        #from github.objects import PullRequestReviewComment

        data = self.http.add_comment(self.id, body)

        if data["__typename"] == "CommitComment":
            return CommitComment.from_data(data, self.http)
        elif data["__typename"] == "GistComment":
            return GistComment.from_data(data, self.http)
        elif data["__typename"] == "IssueComment":
            if self.data["__typename"] == "Issue":
                return IssueComment.from_data(data, self.http)
            elif self.data["__typename"] == "PullRequest":
                return PullRequestComment.from_data(data, self.http)
        elif data["__typename"] == "PullRequestReviewComment":
            return PullRequestReviewComment.from_data(data, self.http)
