import datetime
import typing

from github import utils
from github.abc import Actor
from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable


class Bot(Actor, Node, Type, UniformResourceLocatable):
    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self):
        return "<{0.__class__.__name__} login='{0.login}'>".format(self)

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(bot, http) for bot in data]
    
    @property
    def created_at(self):
        """
        The date and time the bot was created.
        """

        return utils.iso_to_datetime(self.data["createdAt"])

    @property
    def database_id(self):
        """
        The bot's primary key from the database.
        """

        return self.data["databaseId"]
    
    @property
    def updated_at(self):
        """
        The date and time the bot was last updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)
