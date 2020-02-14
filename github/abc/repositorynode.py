

class RepositoryNode():
    """
    Represents a node which belongs to a repository.

    https://developer.github.com/v4/interface/repositorynode/

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.Label`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    @property
    def repository(self):
        """
        The repository the node belongs to.
        """

        return self.data["repository"]
