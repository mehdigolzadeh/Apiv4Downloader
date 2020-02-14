import typing

class GitHubError(Exception):
    def __init__(self, message: str, *, data: typing.Optional[dict]=None):
        self.message = message
        self.data = data
        # self.response = response

        # if response is not None:
        #     super().__init__("{0.status}: {1}".format(rmessage))
        # else:
        super().__init__(message)

class HTTPException(GitHubError):
    pass

class Forbidden(HTTPException):
    pass

class Internal(HTTPException):
    pass

class NotFound(HTTPException):
    pass

class Unauthorized(HTTPException):
    pass
