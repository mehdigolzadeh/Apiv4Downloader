from github import apiv4

from datalayer import *

# g = apiv4.GitHub("2224398867be11f4221a33549e4c16857bb3b4f3")

# repo = g.fetch_repo_info("MehdiGol", "pull_request_study")

# for pullrequestDetail in repo.pullrequests.PullrequestDetail:
#     print(pullrequestDetail.comments.body+"\n")
# from datetime import datetime

# print(datetime.utcnow().replace(microsecond=0).isoformat()+"Z")


data = getAllrepos()
for l in data:
    print(l[0])