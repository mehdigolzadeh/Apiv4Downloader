
from .issueDetail import IssueDetail

class Issues():
    
    __slots__ = ("data","_repoId","_type")

    def __init__(self, data,repo, issuetype):
        self.data = data
        self._type = issuetype
        self._repoId = repo

    @property
    def type(self):
        return self._type

    @property
    def repoId(self):
        return self._repoId

    @property
    def issueCount(self):
        return self.data['totalCount']

    @property
    def issueStartCursor(self):
        return self.data['pageInfo']["startCursor"]
    
    @property
    def issueEndCursor(self):
        return self.data['pageInfo']["endCursor"]

    @property
    def issueDetail(self):
        return IssueDetail.from_data(self.data['edges'],self.repoId,self.type)