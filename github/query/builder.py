import textwrap
import typing


class Builder():
    __slots__ = ("name", "type", "_arguments", "_collections", "_fields", "_fragments")

    def __init__(self, *, name: str=None, type: str=None):
        self.name = name
        self.type = type or "query"

        self._arguments = list()
        self._collections = list()
        self._fields = list()
        self._fragments = list()

    @classmethod
    def from_dict(cls, data: dict):
        name = data.get("name", None)
        type = data["type"]

        builder = cls(name=name, type=type)
        
        arguments = data.get("arguments", list())
        for (argument) in arguments:
            argument = QueryArgument.from_dict(argument)
            builder.add_argument(argument)
        
        collections = data.get("collections", list())
        for (collection) in collections:
            collection = Collection.from_dict(collection)
            builder.add_collection(collection)
        
        fields = data.get("fields", list())
        for (field) in fields:
            field = Field.from_dict(field)
            builder.add_field(field)
        
        fragments = data.get("fragments", list())
        for (fragment) in fragments:
            fragment = Fragment.from_dict(fragment)
            builder.add_fragment(fragment)

        return builder

    @property
    def arguments(self):
        return self._arguments

    @property
    def collections(self):
        return self._collections

    @property
    def fields(self):
        return self._fields

    @property
    def fragments(self):
        return self._fragments

    def add_argument(self, argument: "QueryArgument"):
        if not isinstance(argument, QueryArgument):
            raise TypeError("argument should be of type QueryArgument")

        self._arguments.append(argument)
        return self

    def add_collection(self, collection: "Collection"):
        if not isinstance(collection, Collection):
            raise TypeError("collection should be of type Collection")

        self._collections.append(collection)
        return self

    def add_field(self, field: "Field"):
        if not isinstance(field, Field):
            raise TypeError("field should be of type Field")

        self._fields.append(field)
        return self

    def add_fragment(self, fragment: "Fragment"):
        if not isinstance(fragment, Fragment):
            raise TypeError("fragment should be of type Fragment")

        self._fragments.append(fragment)
        return self

    def build(self):
        if not self._collections and not self._fields:
            raise RuntimeError("query is missing collections or fields")

        if self.name is not None:
            query = "{0.type} {0.name} ".format(self)
        else:
            query = "{0.type} ".format(self)

        if self._arguments:
            query += "("
            query += ", ".join([argument.build() for argument in self._arguments])
            query += ") "

        query += "{\n"

        for (collection) in self._collections:
            collection = collection.build()
            collection = textwrap.indent(collection, "  ")
            query += "{0}\n".format(collection)

        for (field) in self._fields:
            field = field.build()
            query += "  {0}\n".format(field)

        query += "}"

        for (fragment) in self._fragments:
            fragment = fragment.build()
            query += "\n\n"
            query += fragment

        return query

    def copy(self):
        return Builder.from_dict(self.to_dict())

    def to_dict(self):
        data = dict()

        if self.name is not None:
            data["name"] = self.name

        data["type"] = self.type

        if self._arguments:
            data["arguments"] = [a.to_dict() for a in self._arguments]

        if self._collections:
            data["collections"] = [c.to_dict() for c in self._collections]

        if self._fields:
            data["fields"] = [f.to_dict() for f in self._fields]

        if self._fragments:
            data["fragments"] = [f.to_dict() for f in self._fragments]

        return data

class Query(Builder):
    __slots__ = ("name", "type", "_arguments", "_collections", "_fields", "_fragments")

    def __init__(self, *, name: str=None):
        super().__init__(name=name, type="query")


class Collection():
    __slots__ = ("name", "alias", "_arguments", "_collections", "_fields", "_fragments")

    def __init__(self, *, name: str, alias: str=None):
        self.name = name
        self.alias = alias

        self._arguments = list()
        self._collections = list()
        self._fields = list()
        self._fragments = list()

    @classmethod
    def from_dict(cls, data: dict):
        name = data["name"]
        alias = data.get("alias", None)

        collection = cls(name=name, alias=alias)
        
        arguments = data.get("arguments", list())
        for (argument) in arguments:
            argument = CollectionArgument.from_dict(argument)
            collection.add_argument(argument)
        
        collections = data.get("collections", list())
        for (collection) in collections:
            collection = Collection.from_dict(collection)
            collection.add_collection(collection)
        
        fields = data.get("fields", list())
        for (field) in fields:
            field = Field.from_dict(field)
            collection.add_field(field)

        fragments = data.get("fragments", list())
        for (fragment) in fragments:
            fragment = Fragment.from_dict(fragment)
            collection.add_fragment(fragment)

        return collection

    @property
    def arguments(self):
        return self._arguments

    @property
    def collections(self):
        return self._collections

    @property
    def fields(self):
        return self._fields

    @property
    def fragments(self):
        return self._fragments

    def add_argument(self, argument: "CollectionArgument"):
        if not isinstance(argument, CollectionArgument):
            raise TypeError("argument should be of type CollectionArgument")

        self._arguments.append(argument)
        return self

    def add_collection(self, collection: "Collection"):
        if not isinstance(collection, Collection):
            raise TypeError("collection should be of type Collection")

        if collection is self:
            # prevent recursion
            collection = collection.copy()

        self._collections.append(collection)
        return self

    def add_field(self, field: "Field"):
        if not isinstance(field, Field):
            raise TypeError("field should be of type Field")

        self._fields.append(field)
        return self

    def add_fragment(self, fragment: "Fragment"):
        if not isinstance(fragment, Fragment):
            raise TypeError("fragment should be of type Fragment")

        self._fragments.append(fragment)
        return self

    def build(self):
        if not self._collections and not self._fields and not self._fragments:
            raise RuntimeError("collection '{0.name}' is missing collections, fields or fragments".format(self))

        if self.alias is not None:
            collection = "{0.alias}: {0.name} ".format(self)
        else:
            collection = "{0.name} ".format(self)

        if self._arguments:
            collection += "("
            collection += ", ".join([argument.build() for argument in self._arguments])
            collection += ") "

        collection += "{\n"

        for (fragment) in self._fragments:
            if fragment.inline:
                fragment = fragment.build_inline()
                fragment = textwrap.indent(fragment, "  ")
                collection += "{0}\n".format(fragment)
            else:
                fragment = "... {0.name}".format(fragment)
                collection += "  {0}\n".format(fragment)


        for (collection_) in self._collections:
            collection_ = collection_.build()
            collection_ = textwrap.indent(collection_, "  ")
            collection += "{0}\n".format(collection_)


        for (field) in self._fields:
            field = field.build()
            collection += "  {0}\n".format(field)

        collection += "}"

        return collection

    def copy(self):
        """
        Creates a shallow-copy of this object.

        Returns
        -------
        :class:`~query.Collection`
            The new object.
        """

        return Collection.from_dict(self.to_dict())

    def to_dict(self):
        """
        Creates a dict object from this
        :class:`~query.Collection`.

        Returns
        -------
        :class:`dict`
            The dict object.
        """

        data = dict()

        data["name"] = self.name

        if self.alias is not None:
            data["alias"] = self.alias

        if self._arguments:
            data["arguments"] = [a.to_dict() for a in self._arguments]

        if self._collections:
            data["collections"] = [c.to_dict() for c in self._collections]

        if self._fields:
            data["fields"] = [f.to_dict() for f in self._fields]

        if self._fragments:
            data["fragments"] = [f.to_dict() for f in self._fragments]

        return data

class CollectionArgument():

    __slots__ = ("name", "value")

    def __init__(self, *, name: str, value: str):
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, data: dict):

        name = data["name"]
        value = data["value"]

        argument = cls(name=name, value=value)
        return argument

    def build(self):
        argument = "{0.name}: {0.value}".format(self)
        return argument

    def copy(self):
        return CollectionArgument.from_dict(self.to_dict())

    def to_dict(self):
        data = dict()

        data["name"] = self.name
        data["value"] = self.value

        return data

class Field():
    __slots__ = ("name", "alias")

    def __init__(self, *, name: str, alias: str=None):
        self.name = name
        self.alias = alias

    @classmethod
    def from_dict(cls, data: dict):

        name = data["name"]
        alias = data.get("alias", None)

        field = cls(name=name, alias=alias)
        return field

    def build(self):
        if self.alias is not None:
            field = "{0.alias}: {0.name}".format(self)
        else:
            field = "{0.name}".format(self)

        return field

    def copy(self):
        return Field.from_dict(self.to_dict())

    def to_dict(self):
        data = dict()

        data["name"] = self.name

        if self.alias is not None:
            data["alias"] = self.alias

        return data

class Fragment():
    __slots__ = ("name", "type", "inline", "_collections", "_fields", "_fragments")

    def __init__(self, *, name: str, type: str, inline: bool=True):
        self.name = name
        self.type = type
        self.inline = inline

        self._collections = list()
        self._fields = list()
        self._fragments = list()

    @classmethod
    def from_dict(cls, data: dict):

        name = data["name"]
        type = data["type"]
        inline = data["inline"]

        fragment = cls(name=name, type=type, inline=inline)
        
        collections = data.get("collections", list())
        for (collection) in collections:
            collection = Collection.from_dict(collection)
            fragment.add_collection(collection)
        
        fields = data.get("fields", list())
        for (field) in fields:
            field = Field.from_dict(field)
            fragment.add_field(field)
        
        fragments = data.get("fragments", list())
        for (fragment_) in fragments:
            fragment_ = Fragment.from_dict(fragment_)
            fragment.add_fragment(fragment_)

        return fragment

    @property
    def collections(self):
        return self._collections

    @property
    def fields(self):
        return self._fields

    @property
    def fragments(self):
        return self._fragments

    def add_collection(self, collection: Collection):
        if not isinstance(collection, Collection):
            raise TypeError("collection should be of type Collection")

        self._collections.append(collection)
        return self

    def add_field(self, field: Field):
        if not isinstance(field, Field):
            raise TypeError("field should be of type Field")

        self._fields.append(field)
        return self

    def add_fragment(self, fragment: "Fragment"):
        if not isinstance(fragment, Fragment):
            raise TypeError("fragment should be of type Fragment")

        if fragment is self:
            # prevent recursion
            fragment = fragment.copy()

        self._fragments.append(fragment)
        return self

    def build(self):
        if not self._collections and not self._fields and not self._fragments:
            raise RuntimeError("fragment {0.name} is missing collections, fields or fragments".format(self))

        fragment = "fragment {0.name} on {0.type} ".format(self)
        fragment += "{\n"


        for (fragment_) in self._fragments:
            fragment_ = fragment_.build_inline()
            fragment_ = textwrap.indent(fragment_, "  ")
            fragment += "{0}\n".format(fragment_)


        for (collection) in self._collections:
            collection = collection.build()
            collection = textwrap.indent(collection, "  ")
            fragment += "{0}\n".format(collection)

        for (field) in self._fields:
            field = field.build()
            fragment += "  {0}\n".format(field)


        fragment += "}"

        return fragment

    def build_inline(self):
        if self._fragments:
            raise RuntimeError("inline fragments cannot be nested")

        if not self._collections and not self._fields:
            raise RuntimeError("fragment {0.name} is missing collections or fields".format(self))

        fragment = "... on {0.type} ".format(self)
        fragment += "{\n"

        for (collection) in self._collections:
            collection = collection.build()
            collection = textwrap.indent(collection, "  ")
            fragment += "{0}\n".format(collection)

        for (field) in self._fields:
            field = field.build()
            fragment += "  {0}\n".format(field)

        fragment += "}"

        return fragment

    def copy(self):
        return Fragment.from_dict(self.to_dict())

    def to_dict(self):
        data = dict()

        data["name"] = self.name
        data["type"] = self.type
        data["inline"] = self.inline

        if self._collections:
            data["collections"] = [c.to_dict() for c in self._collections]

        if self._fields:
            data["fields"] = [f.to_dict() for f in self._fields]

        if self._fragments:
            data["fragments"] = [f.to_dict() for f in self._fragments]

        return data

class QueryArgument():
    __slots__ = ("name", "type", "default")

    def __init__(self, *, name: str, type: str, default: str=None):
        self.name = name
        self.type = type
        self.default = default

    @classmethod
    def from_dict(cls, data: dict):
        name = data["name"]
        type = data["type"]
        default = data.get("default", None)

        argument = cls(name=name, type=type, default=default)
        return argument

    def build(self):
        if self.default is not None:
            argument = "{0.name}: {0.type}={0.default}".format(self)
        else:
            argument = "{0.name}: {0.type}".format(self)

        return argument

    def copy(self):
        return QueryArgument.from_dict(self.to_dict())

    def to_dict(self):
        data = dict()

        data["name"] = self.name
        data["value"] = self.value

        if self.default is not None:
            data["default"] = self.default

        return data
