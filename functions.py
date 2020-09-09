import json

# ..........
def getToken():
    with open("./config.json","r") as config:
        config = json.loads(config.read())
    return config["token"]