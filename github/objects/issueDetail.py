from .comments import Comments
from github import utils

class IssueDetail():
    
    __slots__ = ("data","_repoId","_type")

    def __init__(self, data, repo, issuetype):
        self.data = data
        self._repoId = repo
        self._type = issuetype

    @classmethod
    def from_data(cls, data, repo, issuetype):
        if isinstance(data, dict):
            return cls(data,repo,issuetype)
        elif isinstance(data, list):
            return [ cls(IssueDetail,repo,issuetype) for IssueDetail in data]

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
        authordata = self.data["node"]['author']
        
        if isinstance(authordata, dict) and "login" in authordata :
            return self.data["node"]['author']["login"]
        else:
            return None
    
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
    def closedAt(self):
        try:
            return utils.iso_to_datetime( self.data["node"]['closedAt'])
        except:
            return None

    @property
    def participants(self):
        return self.data["node"]['participants']['totalCount']

    @property
    def type(self):
        return self._type

    @property
    def state(self):
        return self.data["node"]['state']

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
        return Comments.from_data(self.data["node"]['comments']['edges'],self.id)

    
    # id, cursor, repoId, author, number, title, \
    # body, createdAt, closedAt, participants, type ,status,\
    # commentCount, commentStartCursor, commentEndCursor

    @property
    def getIssueInfo(self):
        return (self.id,self.cursor,self.repoId,self.author,self.number,
                    self.title, self.body,self.createdAt,self.closedAt, self.participants,self.type,self.state,
                    self.commentCount, self.commentStartCursor,self.commentEndCursor)
