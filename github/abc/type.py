
class Type():
    """
    Represents an object type.

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Bot`
    * :class:`~github.CodeOfConduct`
    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.Label`
    * :class:`~github.Language`
    * :class:`~github.License`
    * :class:`~github.LicenseRule`
    * :class:`~github.Metadata`
    * :class:`~github.Mannequin`
    * :class:`~github.Organization`
    * :class:`~github.PullRequest`
    * :class:`~github.RateLimit`
    * :class:`~github.Reaction`
    * :class:`~github.Repository`
    * :class:`~github.Topic`
    * :class:`~github.User`
    """

    __slots__ = ()

    @property
    def type(self):
        """
        The object's type.
        """

        return self.data["__typename"]
