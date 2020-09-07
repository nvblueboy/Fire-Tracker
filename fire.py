from datetime import datetime

class Fire:
    def __init__(self):
        self.title = ""
        self.published = ""
        self.pubdate = ""
        self.lat = 0
        self.long = 0
        self.link = ""
        self.guid = ""
        self.description = ""
    
    def __str__(self):
        output = ""
        output += "title:" + self.title + "\n"
        output += "published:" + self.published + "\n"
        output += "pubdate:" + datetime.strftime(self.pubdate, '%m/%d/%Y') + "\n"
        output += "lat:" + str(self.lat) + "\n"
        output += "long:" + str(self.long) + "\n"
        output += "link:" + self.link + "\n"
        output += "guid:" + self.guid + "\n"
        output += "description:" + self.description + "\n"
        return output
        
    def formatAsHtml(self):
        output = ""

        #Format title as link
        output += '<a href="' + self.link + '">'
        output += self.title
        output += "</a>" + "\n"

        #add description
        if self.description != "":
            output += "<br/>\n"
            output += self.description
        else:
            output += "<br/>\nNo Description."

        return output