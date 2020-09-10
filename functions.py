import json


def openRoles():
    with open("./roles.json","r") as rr:
        rr = json.loads(rr.read())
    return rr

def openJson():
    with open("./config.json","r") as config:
        config = json.loads(config.read())
    return config

# ..........
def getToken():
    return openJson()["token"]

#............
def getPrefix():
    return openJson()["prefix"]


#.............
def splitRoles(roles):
    l = openRoles()
    return roles