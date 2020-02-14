import datetime

from github import utils
from github.abc import Type


class RateLimit(Type):
    """
    Represents the viewer's rate limit.

    https://developer.github.com/v4/object/ratelimit/

    Implements:

    * :class:`~abc.Type`
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self) :
        return "<{0.__class__.__name__} limit={0.limit} remaining={0.remaining}>".format(self)

    @classmethod
    def from_data(cls, data):
        return cls(data)

    @property
    def limit(self) :
        """
        The maximum number of points the viewer is permitted to consume in a rate limit window.
        """

        return self.data["limit"]

    @property
    def remaining(self) :
        """
        The number of points remaining in the current rate limit window.
        """

        return self.data["remaining"]

    @property
    def reset_at(self):
        """
        The date and time at which the current rate limit window resets in UTC.
        """

        reset_at = self.data["resetAt"]
        return utils.iso_to_datetime(reset_at)
