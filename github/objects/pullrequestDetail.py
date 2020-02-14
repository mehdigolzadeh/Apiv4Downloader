from .comments import Comments
from github import utils

class PullrequestDetail():
    
    __slots__ = ("data","_repoid")

    def __init__(self, data,repo):
        self.data = data
        self._repoid = repo

    @classmethod
    def from_data(cls, data,repoId):
        if isinstance(data, dict):
            return cls(data,repoId)
        elif isinstance(data, list):
            return [cls(PullrequestDetail,repoId) for PullrequestDetail in data]

    @property
    def repoId(self):
        return self._repoId

    @property
    def cursor(self):
        return self.data['cursor']
    
    @property
    def id(self):
        return self.data["node"]['id']

    @property
    def author(self):
        return self.data["node"]['author']["login"]
    
    @property
    def body(self):
        return self.data["node"]['body']

    @property
    def number(self):
        return self.data["node"]['number']

    @property
    def title(self):
        return self.data["node"]['title']

    @property
    def createdAt(self):
        return utils.iso_to_datetime( self.data["node"]['createdAt'])

    @property
    def participants(self):
        return self.data["node"]['participants']['totalCount']

    @property
    def commentCount(self):
        return self.data["node"]['comments']['totalCount']
    
    @property
    def commentStartCursor(self):
        return self.data["node"]['comments']['pageInfo']['startCursor']

    @property
    def commentEndCursor(self):
        return self.data["node"]['comments']['pageInfo']['endCursor']

    @property
    def comments(self):
        return Comments.from_data(self.data["node"]['comments']['edges'])

    @property
    def getPullrequestInfo(self,repoid):
        return (self.id,self.cursor,self.repoid,self.author,self.number,
                    self.title, self.body,self.createdAt,self.participants,
                    self.commentCount, self.commentStartCursor,self.commentEndCursor)