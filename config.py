import json
import os.path

class config:
    def __init__(self):
        if os.path.exists("config.json"):
            fileHandle = open("config.json", "r")
            self.readFile(fileHandle.read())
            fileHandle.close()
        else:
            self.useDefaults()

    
    def useDefaults(self):
        self.location = (37.8199, -122.4783)
        self.distance = 100
        self.email = 'test@example.com'
        self.days = 5

    def readFile(self, fileData):
        jsondata = json.loads(fileData)

        self.location = (jsondata["location"]["lat"], jsondata["location"]["long"])
        self.distance = jsondata["distance"]
        self.email = jsondata["email"]
        self.days = jsondata["days"]
        self.email_sender = jsondata["email"]["smtp"]["sender"]
        self.smtp_server = jsondata["email"]["smtp"]["server"]
        self.smtp_user = jsondata["email"]["smtp"]["username"]
        self.smtp_pass = jsondata["email"]["smtp"]["password"]
        self.addresses = jsondata["email"]["addresses"]
