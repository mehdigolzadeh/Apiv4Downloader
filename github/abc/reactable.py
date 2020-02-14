import typing

from github.enums import Reaction as reaction_enum


class Reactable():
    """
    Represents an object which can be reacted to.

    https://developer.github.com/v4/interface/reactable/

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    @property
    def reactions(self):
        """
        A list of :class:`~github.Reaction`.
        """

        # prevent cyclic imports
        from github.objects import Reaction

        reactions = self.data["reactionGroups"]
        return Reaction.from_data(reactions, self.http)

    @property
    def viewer_can_react(self) :
        """
        Whether or not the authenticated user can react to this
        reactable.
        """

        return self.data["viewerCanReact"]

    def add_reaction(self, reaction: str):
        """
        |coro|

        Adds a reaction to the reactable.

        Example
        -------

        .. code:: py

            comment = g.fetch_node("MDU6SXNzdWU0Nzg1MzgwMzA=")
            comment.add_reaction(enums.Reaction.EYES)

        Parameters
        ----------
        reaction: :class:`str`
            The reaction to add.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to add reactions to the
            reactable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The reactable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        if reaction not in reaction_enum._dict.keys():
            reaction = reaction_enum._dict_flipped[reaction]
            
        # TODO: implement HTTPClient.add_reaction
        ...

    def remove_reaction(self, reaction: str):
        """
        |coro|

        Removes a reaction from the reactable.

        Example
        -------

        .. code:: py

            comment = g.fetch_node("MDU6SXNzdWU0Nzg1MzgwMzA=")
            comment.remove_reaction(enums.Reaction.EYES)

        Parameters
        ----------
        reaction: :class:`str`
            The reaction to remove.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to remove reactions from the
            reactable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The reactable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        if reaction not in reaction_enum._dict.keys():
            reaction = reaction_enum._dict_flipped[reaction]
            
        # TODO: implement HTTPClient.remove_reaction
        ...
