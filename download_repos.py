import csv
from github import apiv4
from datalayer import *
from github import utils
from datetime import datetime
import time

# g = apiv4.GitHub("264f7b46ae543ef4bcde16f82d7044f7f86743cc") 
g = apiv4.GitHub("2224398867be11f4221a33549e4c16857bb3b4f3")

def getNow():
    return utils.iso_to_datetime(datetime.utcnow().replace(microsecond=0).isoformat()+"Z")

def getRepoInfo(nameowner,platform):
    owner = nameowner.split('/')[0]
    name = nameowner.split('/')[1]
    repo = None
    try:
        if owner == 'postcss' and name == 'autoprefixer':
            pass
        repo = g.fetch_repo_info(owner, name)
    except Exception as ex:
        if "Could not resolve to a Repository" in str(ex) :
            insertRepoNotFound(nameowner,platform,owner,name,"Repo not found")
        elif "Could not resolve to a User" in str(ex) :
            insertRepoNotFound(nameowner,platform,owner,name,"User not found")
        else:
            print(str(ex))
            insertError(nameowner,'repo',ex)
        return

    insertRepo(repo,nameowner, platform ,owner,name)

    for issueDetail in repo.issues.issueDetail:
        insertIssue(issueDetail,nameowner)
        insertIssueComment(issueDetail.id,issueDetail.author,issueDetail.createdAt,getNow(),issueDetail.body,nameowner)
        for comment in issueDetail.comments:
            insertComment(comment,nameowner)

    for issueDetail in repo.pullrequests.issueDetail:
        insertIssue(issueDetail,nameowner)
        insertIssueComment(issueDetail.id,issueDetail.author,issueDetail.createdAt,getNow(),issueDetail.body,nameowner)
        for comment in issueDetail.comments:
            insertComment(comment,nameowner)

# getRepoInfo('zetmann/repo')

# try:
#     getRepoInfo("theDweeb",'Portfolio')
# except Exception as ex:
#     insertError("","","repo",ex)




i = 0
with open('packagerepos.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        
        nameowner = row[9]
        platform = row[2]


        if( nameowner == "Repository Name with Owner"):
            continue
        i+=1
        if nameowner in getAllrepos():
            continue
        
        getRepoInfo(nameowner,platform)
        
        # time.sleep(.65)
        


