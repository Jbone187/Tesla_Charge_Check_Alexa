import json
import time
import schedule
import requests


def schedule_run():

    def req1():
        url = "https://api.tessie.com"

        headers = {
            "accept": "application/json",
            "authorization": "Bearer"
        }

        response = requests.get(url, headers=headers)

        data = response.json()

        tesla_location_return = data["saved_location"]

        # print(tesla_location_return)

        if tesla_location_return == "Home":

            return "Home"

        else:

            return "No Data"

    def req2():
        url = "https://api.tessie.com/"

        headers = {
            "accept": "application/json",
            "authorization": "Bearer"
        }

        response = requests.get(url, headers=headers)

        data = response.json()

        # print(data)

        # print(data['charge_state']['charge_enable_request'])

        # print(data['charge_state']['battery_level'])

        tesla_battery_level = data['charge_state']['battery_level']

        tesla_chargestatus_return = data['charge_state']["charging_state"]

        tesla_charging_request = data['charge_state']['charge_enable_request']

        tesla_charge_port_door_open = data['charge_state']['charge_port_door_open']

        # print(tesla_chargestatus_return)

        if tesla_chargestatus_return == "Stopped" and tesla_charge_port_door_open == False:

            return "Tesla is not Charging"

        elif tesla_chargestatus_return == "Complete" and tesla_battery_level == 100:

            return "Tesla Charging is complete at 100%"

        elif tesla_chargestatus_return == "Stopped" and tesla_charge_port_door_open == True:

            return "Tesla Charging is on Standby"

        elif tesla_chargestatus_return == "Charging":

            return "Tesla is Charging"

        elif tesla_chargestatus_return == "Disconnected":

            return "Disconnected"

    def req3():
        url = "https://api.virtualbuttons.com/"

        accesscode = "amzn1"

        body = json.dumps({

            "virtualButton": 1,
            "accessCode": accesscode

        })

        requests.post(url, data=body)

    answer1 = req1()
    answer2 = req2()

    # print(answer1)
    # print(answer2)

    def finalTest():

        if answer1 == "Home" and answer2 == "Tesla is not Charging":

            req3()

            print("Tesla is not Charging")

        elif answer1 == "Home" and answer2 == "Disconnected":

            req3()

            print("Tesla is not Charging")

        elif answer2 == "Tesla Charging is complete at 100%":

            print("Tesla Charging is complete at 100%")

        elif answer2 == "Tesla is Charging":

            print("Tesla is Charging")

        elif answer2 == "Tesla Charging is on Standby":

            print("Tesla Charging is on Standby")

    finalTest()


schedule.every(45).seconds.do(schedule_run)

while True:
    schedule.run_pending()
    time.sleep(1)

schedule_run()
