from fire import Fire
from vincenty import vincenty
from datetime import datetime, timedelta
from config import config

def filter(fireList):
    output = []

    configObject = config()



    #get the date to look forward from
    sinceDate = datetime.now() - timedelta(days=configObject.days)

    for fire in fireList:
        fireloc = (fire.lat, fire.long)

        fireDist = vincenty(configObject.location, fireloc)

        if fireDist <= configObject.distance and fire.pubdate > sinceDate:
            output.append(fire)
    
    return output