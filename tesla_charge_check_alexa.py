import json
import requests


def req1():
    url = "https://api.tessie.com/XXXXXXXXXXX/location"
    
    headers = {
    "accept": "application/json",
    "authorization": "Bearer XXXXXXXXXXXXXXXX"
    }
    response = requests.get(url, headers=headers)
    
    data = response.json()

    tesla_location_return = data["saved_location"]

    if tesla_location_return == "Home":

        return "Home_Answer"
        
    else:

        return "No Data"

def req2():
    url = "https://api.tessie.com/XXXXXXXXXXXXXX/state?use_cache=true"
    
    headers = {
    "accept": "application/json",
    "authorization": "Bearer XXXXXXXXX"
    }
    response = requests.get(url, headers=headers)

    data = response.json()

    tesla_chargestatus_return = data['charge_state']["charging_state"]

    #print(tesla_chargestatus_return)

    if tesla_chargestatus_return == "Disconnected" or tesla_chargestatus_return == "Stopped":

        return "Charging_Answer"
        
    else:

        return "No Data"

def req3():
    url = "https://api.virtualbuttons.com/v1?"

    accesscode = "XXXXXXXXXX"
    
    body = json.dumps({
        
        "virtualButton": 1,
        "accessCode": accesscode
        
        })
        
    requests.post(url, data = body)


answer1 = req1()
answer2 = req2()

def finalTest():

    if answer1 == "Home_Answer" and answer2 == "Charging_Answer":

        req3()
        
        print("Tesla is not Charging")

    else:

        print("Tesla is Charging")

finalTest()


