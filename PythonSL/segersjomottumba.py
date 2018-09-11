import requests

def SegersjoMotTumba():
    r = requests.get("http://api.sl.se/api2/realtimedeparturesV4.json?key=f96d6c1868c4430a9d631ef0d1c7701b&siteid=7263&timewindow=60")
    j = r.json()
    print(r.status_code)
    buses = j['ResponseData']['Buses']
    for bus in buses:
        if bus['JourneyDirection'] == 2:
            print(bus['Destination'] + " : " + bus['DisplayTime'])


