class Reaction:
    """
    Represents a GitHub reaction.

    https://developer.github.com/v4/enum/reactioncontent/
    """

    _dict = {
        "CONFUSED": "\U0001f615",
        "EYES": "\U0001f440",
        "HEART": "\U00002764",
        "HOORAY": "\U0001f389",
        "LAUGH": "\U0001f604",
        "ROCKET": "\U0001f680",
        "THUMBS_DOWN": "\U0001f44e",
        "THUMBS_UP": "\U0001f44d",
    }

    _dict_flipped = dict()

for (name, emoji) in Reaction._dict.items():
    setattr(Reaction, name, emoji)
    Reaction._dict_flipped[emoji] = name
