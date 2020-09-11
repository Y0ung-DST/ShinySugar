import json


def openRoles():
    with open("./roles.json","r") as rr:
        rr = json.loads(rr.read())
    return rr

def openJson():
    with open("./config.json","r") as config:
        config = json.loads(config.read())
    return config


#..........
def arrtoText(arr):
    # return "".join(i for i in arr)
    if len(arr) == 1:
        return "".join(i for i in arr)
    else:
        return ",".join(i for i in arr)

# ..........
def getToken():
    return openJson()["token"]

#............
def getPrefix():
    return openJson()["prefix"]


#.............
def splitRoles(roles):
    data = {
        "regions": [],
        "gendre": [],
        "likes": [],
        "sexuality": [],
        "ages": [],
        "statue": [],
        "prefers":[]
    }
    l = openRoles()
    for j in l:
        for x in l[j]:
            if x in roles:
                data[j].append(x)
    error = 0
    for j in data:
        if len(data[j]) < 1:
            error = 1
            break
    if error != 1:
        return data
    else:
        return "Complete your profile please."