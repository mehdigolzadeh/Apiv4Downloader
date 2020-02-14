
class Deletable():
    """
    Represents an object which can be deleted.

    https://developer.github.com/v4/interface/deletable/

    Implemented by:

    * :class:`~github.CommitComment`
    """

    __slots__ = ()

    @property
    def viewer_can_delete(self):
        """
        Whether or not the authenticated user can delete the deletable.
        """

        return self.data["viewerCanDelete"]

    def delete(self):
        
        if self.data["__typename"] == "CommitComment":
            # TODO: implement HTTPClient.delete_commit_comment
            ...
        elif self.data["__typename"] == "GistComment":
            # TODO: implement HTTPClient.delete_gist_comment
            ...
        elif self.data["__typename"] == "IssueComment":
            # TODO: implement HTTPClient.delete_issue_comment
            ...
        elif self.data["__typename"] == "PullRequestReview":
            # TODO: implement HTTPClient.delete_pull_request_review
            ...
        elif self.data["__typename"] == "PullRequestReviewComment":
            # TODO: implement HTTPClient.delete_pull_request_review_comment
            ...
        elif self.data["__typename"] == "TeamDiscussion":
            # TODO: implement HTTPClient.delete_team_discussion
            ...
        elif self.data["__typename"] == "TeamDiscussionComment":
            # TODO: implement HTTPClient.delete_team_discussion_comment
            ...
