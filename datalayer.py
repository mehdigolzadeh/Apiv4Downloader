import mysql.connector
from github.objects import Repoinfo
from github import utils
from datetime import datetime

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysqladminpass",
  database="GithubRepository"
)

def insertError(ownerandname,table,exceptionMessage):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO error (ownerandname, onTable, exceptionMessage, occurredAt) VALUES (%s, %s, %s ,%s)"
        cursor.execute(sql, (ownerandname,table,str(exceptionMessage),utils.iso_to_datetime(datetime.utcnow().replace(microsecond=0).isoformat()+"Z")))
        db.commit()
    except Exception as ex:
        print("repo: {} , table: {} , Exc: {}".format(ownerandname,table,str(ex)))

def insertRepo(repoinfo,nameowner,platform,owner,name):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO repository (ownerandname,platform, databaseId, name, owner, createdAt, pushedAt, extractedAt,\
                                    primaryLanguage, languages, commitComments, forkCount,\
                                    isArchived, isLocked, isMirror, stargazers,\
                                    watchers, labels, totalIssues, issueStartCursor, issueEndCursor,\
                                    totalPullrequests, pullrequestStartCursor, pullrequestEndCursor) \
                                    VALUES \
                                    (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (nameowner,platform,) + repoinfo.getRepoInfo)
        db.commit()
    except Exception as ex:
        insertError(nameowner,"repo",ex)

def insertRepoNotFound(nameowner,platform,owner,name,reason):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO repository (ownerandname, platform, name, owner,extractedAt,primaryLanguage) \
                                    VALUES \
                                    (%s, %s,%s, %s, %s, %s)"
        cursor.execute(sql, (nameowner,platform,name,owner,utils.iso_to_datetime(datetime.utcnow().replace(microsecond=0).isoformat()+"Z"),reason))
        db.commit()
    except Exception as ex:
        insertError(nameowner,"repo",ex)

def insertIssue(issueDetail,ownerandname):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO issue (id, pgcursor, repoId, author, issueNumber, title,\
                                    body, createdAt, closedAt, participants, issueType ,issueStatus,\
                                    commentCount, commentStartCursor, commentEndCursor) \
                                    VALUES \
                                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, issueDetail.getIssueInfo)
        db.commit()
    except Exception as ex:
        insertError(ownerandname,'issue',ex)


def insertIssueComment(pid,author,cretedAt,extractedAt,body,ownerandname):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO comment (parentId, pgcursor , author, createdAt, extractedAt, body) \
                                    VALUES \
                                    (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (pid,pid,author,cretedAt,extractedAt,body))
        db.commit()
    except Exception as ex:
        insertError(ownerandname,'comment',ex)

def insertComment(comment,ownerandname):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO comment (parentId, pgcursor , author, createdAt, extractedAt, body) \
                                    VALUES \
                                    (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, comment.getCommentInfo)
        db.commit()
    except Exception as ex:
        insertError(ownerandname,'comment',ex)

def getAllrepos():
    cursor = db.cursor()
    cursor.execute("SELECT ownerandname FROM repository")
        
    return [x[0] for x in cursor.fetchall()]

def getAllUnsuccess():
    cursor = db.cursor()
    cursor.execute("SELECT ownerandname FROM error")
        
    return [x[0] for x in cursor.fetchall()]


# mycursor = db.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")