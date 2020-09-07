import requests
import xml.etree.ElementTree as ET
from fire import Fire
from datetime import datetime, timedelta

namespaces = {"geo" : "http://www.w3.org/2003/01/geo/wgs84_pos#"}
pubDateFormat = '%d %b %Y'

def getRSSData():
    url = "https://inciweb.nwcg.gov/feeds/rss/incidents/"

    r = requests.get(url)

    if r.status_code == 200:
        return r.text
    else:
        return None

def parseXML(rssData):
    root = ET.fromstring(rssData)

    output = []

    for child in root.iter("item"):
        f = Fire()
        link = child.find('link')
        if link != None:
            f.link = link.text

        title = child.find('title')
        if  title != None:
            f.title = title.text

        lon = child.find('geo:long', namespaces)
        if lon != None:
            f.long = float(lon.text)

        lat = child.find('geo:lat', namespaces)
        if lat != None:
            f.lat = float(lat.text)

        guid = child.find('guid')
        if guid != None:
            f.guid = guid.text

        description = child.find('description')
        if description != None:
            f.description = description.text

        pubDate = child.find('pubDate')
        if pubDate != None:
            f.pubdate = datetime.strptime(pubDate.text.split(", ")[1][:11], pubDateFormat)

        output.append(f)

    return output

if __name__ == "__main__":
    import distanceFilter
    from config import config
    rssData = getRSSData()

    fires = distanceFilter.filter(parseXML(rssData))

    for fire in fires:
        print(fire)
      