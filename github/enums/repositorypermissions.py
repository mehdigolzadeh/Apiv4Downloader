class RepositoryPermissions():
    """
    Represents a user's access level to a repository.

    https://developer.github.com/v4/enum/repositorypermission/
    """

    __slots__ = ("_permission",)

    def __init__(self, permission):
        self._permission = permission

    def __repr__(self):
        return "<{0.__class__.__name__} '{0._permission}'>".format(self)

    @classmethod
    def from_data(cls, permission):
        return cls(permission)
    
    @property
    def administrator(self):
        """
        Can read, clone, and push to this repository. Can also manage
        issues, pull requests, and repository settings, including
        adding collaborators.
        """

        return self._permission in ["ADMIN"]

    @property
    def maintain(self):
        """
        Can read, clone, and push to this repository. Can also manage
        issues, pull requests, and some repository settings.
        """

        return self._permission in ["ADMIN", "MAINTAIN"]

    @property
    def write(self):
        """
        Can read, clone, and push to this repository. Can also manage
        issues and pull requests.
        """

        return self._permission in ["ADMIN", "MAINTAIN", "WRITE"]

    @property
    def triage(self):
        """
        Can read and clone this repository. Can also manage issues and
        pull requests.
        """

        return self._permission in ["ADMIN", "MAINTAIN", "WRITE", "TRIAGE"]

    @property
    def read(self):
        """
        Can read and clone this repository. Can also open and comment
        on issues and pull requests.
        """

        return self._permission in ["ADMIN", "MAINTAIN", "WRITE", "TRIAGE", "READ"]
