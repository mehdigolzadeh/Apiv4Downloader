import typing


class Assignable():
    """
    Represents an object which can be assigned to.

    https://developer.github.com/v4/interface/assignable/

    Implemented by:

    * :class:`github.Issue`
    * :class:`github.PullRequest`
    """

    __slots__ = ()

    def fetch_assignees(self):
        from github.objects import User

        data = self.http.fetch_assignable_assignees(self.id)
        return User.from_data(data, self.http)

    def add_assignees(self, *users: "User"):
        
        users = [user.id for user in users]
        self.http.add_assignees(self.id, users)

    def remove_assignees(self, *users: "User"):
        users = [user.id for user in users]
        self.http.remove_assignees(self.id, users)
