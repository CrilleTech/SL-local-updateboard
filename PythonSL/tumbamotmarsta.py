import requests

def TumbaMotMarsta():
    r = requests.get("http://api.sl.se/api2/realtimedeparturesV4.json?key=*your-api-key-here*&siteid=9524&timewindow=60")
    j = r.json()
    print(r.status_code)
    trains = j['ResponseData']['Trains']
    for train in trains:
        if train["JourneyDirection"] == 2:
            print(train['Destination'] + " : " + train['DisplayTime'])


