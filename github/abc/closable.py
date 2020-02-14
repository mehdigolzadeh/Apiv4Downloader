import datetime
import typing

from github import utils


class Closable():
    __slots__ = ()

    @property
    def closed_at(self):
        closed_at = self.data["closedAt"]

        if closed_at:
            return utils.iso_to_datetime(closed_at)

    @property
    def is_closed(self):
        return self.data["closed"]

    def close(self):
        if self.data["__typename"] == "Issue":
            self.http.close_issue(self.id)
        elif self.data["__typename"] == "PullRequest":
            self.http.close_pull_request(self.id)

    def reopen(self):
        if self.data["__typename"] == "Issue":
            self.http.reopen_issue(self.id)
        elif self.data["__typename"] == "PullRequest":
            self.http.reopen_pull_request(self.id)
