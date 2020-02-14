
from .pullrequestDetail import PullrequestDetail

class Pullrequests():
    
    __slots__ = ("data")

    def __init__(self, data):
        self.data = data

    @property
    def pullrequestCount(self):
        return self.data['totalCount']

    @property
    def pullrequestStartCursor(self):
        return self.data['pageInfo']["startCursor"]
    
    @property
    def pullrequestEndCursor(self):
        return self.data['pageInfo']["endCursor"]

    @property
    def PullrequestDetail(self):
        return PullrequestDetail.from_data(self.data['edges'])