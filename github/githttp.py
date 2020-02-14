import uuid
import requests
from github import errors
from github import query

from github import utils
from datetime import datetime


_DEFAULT_BASE_URL = "https://api.github.com/graphql"
_DEFAULT_USER_AGENT = "mehdigol"


class HTTPClient():

    __slots__ = ("_exception_map", "_token", "_base_url", "_user_agent", "_uuid")

    def __init__(self, token, *, base_url=None, user_agent=None):
        self._exception_map = {
            # HTTP status-code
            401: errors.Unauthorized,

            # GitHub API status-message
            "FORBIDDEN": errors.Forbidden,
            "INTERNAL": errors.Internal,
            "NOT_FOUND": errors.NotFound,
        }
        
        self._uuid = uuid.uuid4()
        self._token = token
        self._base_url = base_url or _DEFAULT_BASE_URL
        self._user_agent = user_agent or _DEFAULT_USER_AGENT.format(self._uuid)

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value: str=None):
        self._base_url = value or _DEFAULT_BASE_URL

    @property
    def user_agent(self):
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value: str=None):
        self._user_agent = value or _DEFAULT_USER_AGENT.format(self._uuid)



    def _request(self, *, method, json, headers):

        if method == 'POST':
            # print(self._token)
            # print(self._user_agent)
            response = requests.post(self.base_url, json=json, headers=headers)
            # if response.status_code not in range(200,300):
                
            #     try:
            #         # even when giving a status-code outside of the
            #         # [200, 300) range gql can still give us json data
            #         # with relevant metadata
            #         data = response.json()
            #         if 'message' in data:
            #             message = data["message"]
            #             raise ValueError(message, data=data)
            #         elif 'errors' in data:
            #             print(data['errors'][0]['message'])
            #             raise ValueError(data['errors'][0]['message'])

            #     except exception as e:
            #         data = None
            #         message = "response failed with status-code {0}".format(response.status)

            #     try:
            #         # handled HTTP status-code
            #         exception = self._exception_map[response.status_code]
            #     except (KeyError) as e:
            #         # arbitrary HTTP status-code
            #         exception = errors.HTTPException

            #     raise exception(message, response=response, data=data)
                
            data = response.json()

            if "errors" in data.keys():
                message = data["errors"][0]["message"]
                
                try:
                    type = data["errors"][0]["type"]
                    exception = self._exception_map[type]
                except (KeyError) as e:
                    exception = errors.GitHubError

                raise exception(message, data=data)

            return data

        else:
            return requests.get(self.base_url)

       
            

    def queryrequest(self, *, json: dict, headers: dict=None):
        
        headers = headers or dict()
        headers.update({"Authorization": "bearer {0}".format(self._token)})
        headers.update({"User-Agent": self._user_agent})
        data = self._request(method="POST", json=json, headers=headers)
        
        return data["data"]

    def fetch_authenticated_user(self):
        json = {
            "query": query.FETCH_AUTHENTICATED_USER,
        }

        data = self.queryrequest(json=json)
        return data["viewer"]



    def fetch_metadata(self):
        json = {
            "query": query.FETCH_METADATA,
        }

        data = self.queryrequest(json=json)
        return data["meta"]

    def fetch_node(self, id):
        variables = {
            "id": id,
        }

        json = {
            "query": query.FETCH_NODE,
            "variables": variables,
        }

        data = self.queryrequest(json=json)
        return data["node"]

    def fetch_nodes(self, ids):
        variables = {
            "ids": ids,
        }

        json = {
            "query": query.FETCH_NODES,
            "variables": variables,
        }

        data = self.queryrequest(json=json)
        return data["nodes"]

    def fetch_organization(self, login):
        variables = {
            "login": login,
        }

        json = {
            "query": query.FETCH_ORGANIZATION,
            "variables": variables,
        }

        data = self.queryrequest(json=json)
        return data["organization"]
    
    def fetch_rate_limit(self):
        json = {
            "query": query.FETCH_RATE_LIMIT,
        }

        data = self.queryrequest(json=json)
        return data["rateLimit"]

    def fetch_repository(self, owner, name):
        variables = {
            "owner": owner,
            "name": name,
        }

        json = {
            "query": query.FETCH_REPOSITORY,
            "variables": variables,
        }

        data = self.queryrequest(json=json)
        return data["repository"]


    def fetch_repository_info(self, owner, name):
        variables = {
            "owner": owner,
            "name": name,
        }

        json = {
            "query": query.FETCH_REPO_INFO,
            "variables": variables,
        }

        data = self.queryrequest(json=json)

        timenow = utils.iso_to_datetime(datetime.utcnow().replace(microsecond=0).isoformat()+"Z")
        resetAt = utils.iso_to_datetime(data['rateLimit']['resetAt'])

        print("Project: {}, Time to reset: {} , remaining: {} ".format(owner+"/"+name,(resetAt-timenow).total_seconds(),data['rateLimit']['remaining']))
        return data["repository"]


    def fetch_topic(self, name):
        variables = {
            "name": name,
        }

        json = {
            "query": query.FETCH_TOPIC,
            "variables": variables,
        }

        data = self.queryrequest(json=json)
        return data["topic"]

    def fetch_user(self, login):
        variables = {
            "login": login,
        }

        json = {
            "query": query.FETCH_USER,
            "variables": variables,
        }

        data = self.queryrequest(json=json)
        return data["user"]

    # secondary queries,
    # these methods are invoked from classes in the abc or
    # objects namespaces

    def fetch_assignable_assignees(self, assignable_id):
        raise NotImplementedError("this method is not yet implemented")

    def fetch_commentable_comments(self, commentable_id):
        raise NotImplementedError("this method is not yet implemented")

    def fetch_issue_participants(self, issue_id):
        raise NotImplementedError("this method is not yet implemented")

    def fetch_label_issues(self, label_id):
        raise NotImplementedError("this method is not yet implemented")

    def fetch_label_pull_requests(self, label_id):
        raise NotImplementedError("this method is not yet implemented")

    def fetch_labelable_labels(self, labelable_id):
        raise NotImplementedError("this method is not yet implemented")

    def fetch_profileowner_email(self, profileowner_id):
        variables = {
            "profileowner_id": profileowner_id,
        }

        json = {
            "query": query.FETCH_PROFILEOWNER_EMAIL,
            "variables": variables,
        }

        data = self.queryrequest(json=json)
        return data["node"]["email"]

    def fetch_pull_request_participants(self, pull_request_id):
        raise NotImplementedError("this method is not yet implemented")

    def fetch_repository_assignable_users(self, repository_id):
        nodes = list()
        
        cursor = "Y3Vyc29yOnYyOjA="
        has_next_page = True

        while has_next_page:
            variables = {
                "repository_id": repository_id,
                "cursor": cursor,
            }

            json = {
                "query": query.FETCH_REPOSITORY_ASSIGNABLE_USERS,
                "variables": variables,
            }

            data = self.queryrequest(json=json)
            nodes.extend(data["node"]["assignableUsers"]["nodes"])

            cursor = data["node"]["assignableUsers"]["pageInfo"]["endCursor"]
            has_next_page = data["node"]["assignableUsers"]["pageInfo"]["hasNextPage"]

        return nodes

    def fetch_repository_collaborators(self, repository_id):
        nodes = list()
        
        cursor = "Y3Vyc29yOnYyOjA="
        has_next_page = True

        while has_next_page:
            variables = {
                "repository_id": repository_id,
                "cursor": cursor,
            }

            json = {
                "query": query.FETCH_REPOSITORY_COLLABORATORS,
                "variables": variables,
            }

            data = self.queryrequest(json=json)
            nodes.extend(data["node"]["collaborators"]["nodes"])

            cursor = data["node"]["collaborators"]["pageInfo"]["endCursor"]
            has_next_page = data["node"]["collaborators"]["pageInfo"]["hasNextPage"]

        return nodes

    def fetch_user_commit_comments(self, user_id):
        nodes = list()
        
        cursor = "Y3Vyc29yOnYyOjA="
        has_next_page = True

        while has_next_page:
            variables = {
                "user_id": user_id,
                "cursor": cursor,
            }

            json = {
                "query": query.FETCH_USER_COMMIT_COMMENTS,
                "variables": variables,
            }

            data = self.queryrequest(json=json)
            nodes.extend(data["node"]["commitComments"]["nodes"])

            cursor = data["node"]["commitComments"]["pageInfo"]["endCursor"]
            has_next_page = data["node"]["commitComments"]["pageInfo"]["hasNextPage"]

        return nodes
