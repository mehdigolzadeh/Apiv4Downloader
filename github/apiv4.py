import typing

from github.githttp import HTTPClient

from github.objects import Repoinfo
from github.objects import User

class GitHub():
    __slots__ = ("http",)

    def __init__(self, token: str, user_agent: str=None,base_url: str=None):
        self.http = HTTPClient(token, base_url=base_url, user_agent=user_agent)

    @property
    def base_url(self):
        return self.http.base_url

    @base_url.setter
    def base_url(self, value: str=None):
        self.http.base_url = value

    @property
    def user_agent(self):
        return self.http.user_agent

    @user_agent.setter
    def user_agent(self, value: str=None):
        self.http.user_agent = value

    def fetch_authenticated_user(self):
        data = self.http.fetch_authenticated_user()
        return AuthenticatedUser.from_data(data, self.http)

    def fetch_metadata(self):
        data = self.http.fetch_metadata()
        return Metadata.from_data(data)

    def fetch_node(self, id: str):
        data = self.http.fetch_node(id)
        return Node.from_data(data)

    def fetch_nodes(self, *ids: str):
        data = self.http.fetch_nodes(ids)
        return Node.from_data(data)

    def fetch_organization(self, login: str):
        data = self.http.fetch_organization(login)
        return Organization.from_data(data, self.http)

    def fetch_rate_limit(self):
        data = self.http.fetch_rate_limit()
        return RateLimit.from_data(data)

    def fetch_repository(self, owner: str, name: str):
        data = self.http.fetch_repository(owner, name)
        return Repository.from_data(data, self.http)

    def fetch_topic(self, name: str):
        data = self.http.fetch_topic(name)
        return Topic.from_data(data)

    def fetch_user(self, login: str):
        data = self.http.fetch_user(login)
        return User.from_data(data, self.http)

    def fetch_repo_info (self, owner: str, name: str):
        data = self.http.fetch_repository_info(owner, name)
        return Repoinfo.from_data(data)
    