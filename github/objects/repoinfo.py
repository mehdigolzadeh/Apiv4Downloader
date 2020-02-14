from datetime import datetime
import typing

from github import utils
from .user import User
from .issues import Issues


class Repoinfo():
    __slots__ = ("data")

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_data(cls, data):
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            return [cls(Repoinfo) for Repoinfo in data]

    @property
    def databaseId(self):
        return self.data['databaseId']

    @property
    def name(self):
        return self.data['name']

    @property
    def owner(self):
        return self.data['owner']['login']

    @property
    def createdAt(self):
        return utils.iso_to_datetime(self.data['createdAt'])

    @property
    def pushedAt(self):
        return utils.iso_to_datetime(self.data['pushedAt'])

    @property
    def extractedAt(self):
        return utils.iso_to_datetime(datetime.utcnow().replace(microsecond=0).isoformat()+"Z")

    @property
    def primaryLanguage(self):
        if isinstance(self.data['primaryLanguage'], dict) and "name" in self.data['primaryLanguage'] :
            return self.data['primaryLanguage']['name']
        else:
            return None

    @property
    def languages(self):
        return self.data["languages"]["totalCount"]
    
    @property
    def commitComments(self):
        return self.data['commitComments']['totalCount']

    @property
    def forkCount(self):
        return self.data['forkCount']

    @property
    def isArchived(self):
        return self.data['isArchived']

    @property
    def isFork(self):
        return self.data['isFork']

    @property
    def isLocked(self):
        return self.data['isLocked']

    @property
    def isMirror(self):
        return self.data['isMirror']

    @property
    def stargazers(self):
        return self.data['stargazers']['totalCount']

    @property
    def watchers(self):
        return self.data['watchers']['totalCount']

    @property
    def labels(self):
        return self.data['labels']['totalCount']

    @property
    def issues(self):
        return Issues(self.data["issues"],self.databaseId,"Issue")

    @property
    def pullrequests(self):
        return Issues(self.data["pullRequests"],self.databaseId,"Pullrequest")


    # return tuple for db

    # databaseId, name, owner, createdAt, pushedAt, extractedAt,\
    # primaryLanguage, languages, commitComments, forkCount,\
    # isArchived, isLocked, isMirror, stargazers,\
    # watchers, labels, totalIssues, issueStartCursor, issueEndCursor,\
    # totalPullrequests, pullrequestStartCursor, pullrequestEndCursor

    @property
    def getRepoInfo(self):
        return (self.databaseId,self.name,self.owner,self.createdAt,self.pushedAt,self.extractedAt,self.primaryLanguage,self.languages,
                    self.commitComments,self.forkCount,self.isArchived,self.isLocked,self.isMirror,self.stargazers,
                    self.watchers,self.labels,self.issues.issueCount,self.issues.issueStartCursor,self.issues.issueEndCursor,
                    self.pullrequests.issueCount,self.pullrequests.issueStartCursor,self.pullrequests.issueEndCursor)