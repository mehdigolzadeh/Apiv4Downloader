class ProjectOwner():
    """
    Represents the owner of a GitHub project.

    https://developer.github.com/v4/interface/projectowner/

    Implemented by:

    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Organization`
    * :class:`~github.Repository`
    * :class:`~github.User`
    """

    __slots__ = ()

    @property
    def projects_resource_path(self):
        """
        The project owner's projects resource path.
        """

        return self.data["projectsResourcePath"]

    @property
    def projects_url(self):
        """
        The project owner's projects url.
        """

        return self.data["projectsUrl"]

    @property
    def viewer_can_create_projects(self):
        """
        Whether or not the authenticated user can create projects in the project owner.
        """

        return self.data["viewerCanCreateProjects"]
    