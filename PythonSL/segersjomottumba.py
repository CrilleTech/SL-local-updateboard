#

import requests
#request lib to read the URI in Json
def SegersjoMotTumba():
    r = requests.get("http://api.sl.se/api2/realtimedeparturesV4.json?key="-youre-api-key-here-"&siteid=7263&timewindow=60")
    j = r.json()
    print(r.status_code) #mostly for debugging
    buses = j['ResponseData']['Buses']
    for bus in buses:
        if bus['JourneyDirection'] == 2:  #journey direction is either 1 or 2 depending on which way the buss travels. 
            print(bus['Destination'] + " : " + bus['DisplayTime']) #print out the buss destination from the bus stop as defined in the siteid in he URI above


