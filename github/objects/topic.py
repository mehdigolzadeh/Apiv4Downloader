import typing

from github.abc import Node
from github.abc import Type


class Topic(Node, Type):
    """
    Represents a GitHub topic.

    https://developer.github.com/v4/object/topic/

    Implements:

    * :class:`~abc.Node`
    * :class:`~abc.Type`
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self) :
        return "<{0.__class__.__name__} name='{0.name}'>".format(self)

    @classmethod
    def from_data(cls, data):
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            return [cls(topic) for topic in data]

    @property
    def name(self) :
        """
        The topic's name.
        """

        return self.data["name"]

    @property
    def related_topics(self):
        """
        A list of related topics.
        """

        related = self.data.get("relatedTopics", None)
        return PartialTopic.from_data(related)

class PartialTopic(Topic):
    """
    Represents a GitHub topic.

    https://developer.github.com/v4/object/topic/

    Implements:

    * :class:`~abc.Node`
    * :class:`~abc.Type`

    Using this partial-class will result in the following attributes being ``None`` at all times:

    * :attr:`~github.Topic.related_topics`
    """

    __slots__ = ("data",)
