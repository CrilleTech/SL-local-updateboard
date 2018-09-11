import requests

def SegersjoMotTumba():
    done = False
    while done == False:
        r = requests.get("https://api.sl.se/api2/realtimedeparturesV4.json?key=*add-api-key-here*&siteid=7263&timewindow=60")
        if CheckError(r.text) == False:
            done = True
            j = r.json()
            #print(r.status_code)
            buses = j['ResponseData']['Buses']
            for bus in buses:
                if bus['JourneyDirection'] == 2:
                    print(bus['Destination'] + " : " + bus['DisplayTime'])
        else:
            done = False

def TumbaMotMarsta():
    done = False
    while done == False:
        r = requests.get("https://api.sl.se/api2/realtimedeparturesV4.json?key=*add-api-key-here*&siteid=9524&timewindow=60")
        if CheckError(r.text) == False:
            done = True
            j = r.json()
            #print(r.status_code)
            trains = j['ResponseData']['Trains']
            for train in trains:
                if train["JourneyDirection"] == 2:
                    print(train['Destination'] + " : " + train['DisplayTime'])
        else:
            done = False

def Deviations():
    r = requests.get("https://api.sl.se/api2/realtimedeparturesV4.json?key=*add-api-key-here*&siteid=9524&timewindow=60&bus=False")
    j = r.json()
    deviations = j['ResponseData']['StopPointDeviations']
    for dev in deviations:
          if dev['Deviation']['ImportanceLevel'] > 2:  #deviations and trafic stops based on the siteid as defined in URI
            print(dev['Deviation']['Text'])

def CheckError(text):
    if text != "":
        if text[0] =='{':
            return False
    
    return True

