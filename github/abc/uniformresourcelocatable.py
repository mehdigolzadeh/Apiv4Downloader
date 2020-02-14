class UniformResourceLocatable():
    """
    Represents an object that can be retrieved by a URL.

    https://developer.github.com/v4/interface/uniformresourcelocatable/

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Bot`
    * :class:`~github.CodeOfConduct`
    * :class:`~github.Issue`
    * :class:`~github.Label`
    * :class:`~github.Mannequin`
    * :class:`~github.Organization`
    * :class:`~github.PullRequest`
    * :class:`~github.Repository`
    * :class:`~github.User`
    """

    __slots__ = ()

    @property
    def resource_path(self):
        """
        The resource path pointing to the resource.
        """

        return self.data["resourcePath"]

    @property
    def url(self):
        """
        The url pointing to the resource.
        """

        return self.data["url"]
