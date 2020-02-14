from github import utils
from datetime import datetime

class Comments():
    
    __slots__ = ("data","_parentId")

    def __init__(self, data, parent):
        self.data = data
        self._parentId = parent

    @classmethod
    def from_data(cls, data, parent):
        if isinstance(data, dict):
            return cls(data,parent)
        elif isinstance(data, list):
            return [cls(Comments,parent) for Comments in data]

    @property
    def parentId(self):
        return self._parentId

    @property
    def cursor(self):
        return self.data['cursor']

    @property
    def author(self):
        authordata = self.data["node"]['author']
        
        if isinstance(authordata, dict) and "login" in authordata :
            return self.data["node"]['author']["login"]
        else:
            return None

    @property
    def createdAt(self):
        return utils.iso_to_datetime(self.data["node"]['createdAt'])

    @property
    def extractedAt(self):
        return utils.iso_to_datetime(datetime.utcnow().replace(microsecond=0).isoformat()+"Z")

    @property
    def body(self):
        return self.data["node"]['body']

    # parentId, cursor , author, createdAt, extractedAt, body
    @property
    def getCommentInfo(self):
        return (self.parentId, self.cursor,self.author,self.createdAt,self.extractedAt,self.body)