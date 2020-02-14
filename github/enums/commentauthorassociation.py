class CommentAuthorAssociation():
    """
    Represents an actor's association with a repository.

    https://developer.github.com/v4/enum/commentauthorassociation/
    """

    __slots__ = ("data",)

    def __init__(self, author_association):
        self._author_association = author_association

    def __repr__(self):
        return "<{0.__class__.__name__} '{0._author_association}'>".format(self)

    @classmethod
    def from_data(cls, author_association):
        return cls(author_association)

    @property
    def owner(self):
        """
        The actor is the owner of the repository.
        """

        return self._author_association == "OWNER"

    @property
    def member(self):
        """
        The actor is a member of the organization that owns the repository.
        """

        return self._author_association == "MEMBER"

    @property
    def collaborator(self):
        """
        The actor has been invited to collaborate on the repository.
        """

        return self._author_association == "COLLABORATOR"

    @property
    def contributor(self):
        """
        The actor has previously committed to the repository.
        """

        return self._author_association == "CONTRIBUTOR"

    @property
    def first_time_contributor(self):
        """
        The actor has not previously committed to this repository.
        """

        return self._author_association == "FIRST_TIME_CONTRIBUTOR"

    @property
    def first_timer(self):
        """
        The actor has not previously committed to GitHub.
        """

        return self._author_association == "FIRST_TIMER"

    @property
    def none(self):
        """
        The actor has no association with the repository.
        """

        return self._author_association == "NONE"
