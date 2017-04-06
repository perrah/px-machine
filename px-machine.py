#imports for code
import time
import datetime
import os
import json
import requests
from sense_hat import SenseHat

#set variables for data uploads
url = "https://etc-px-api.run.aws-usw02-pr.ice.predix.io/dataPoints"

attributes = {
    "SysId" : "etcPi",
    "Region" : "HeathersDesk",
    "Owner" : "DTLPs"
}

proxies = {
    "http" : "3.28.29.241:88",
    "https" : "3.28.29.241:88"
}

headers = {
    "content-type" : "application/json",
    "x-clientid" : "healthcare_etc-px-api_prod",
    "x-base64-credentials" : "Basic TOKEN_HERE",
    "cache-control" : "no-cache"
}

#set sense hat variables
sense = SenseHat()

# Output temp sensor reading (shared with humidity sensor)
# Assumes senseHat library already loaded above
while True:

    timeStamp = int(time.time() * 1000)

    try:
        temp = sense.get_temperature()
        temp = round(temp, 1)

        data = {
            "body": [{
		"name": "ETC_PX_TRAINING",
		"datapoints": [
			[
				timeStamp,
				temp,
				3
			]
		],
		"attributes": attributes
            }]
        }#end data json


        data_json = json.dumps(data)
        print(data_json)
        data_post = requests.post(url, data_json, headers=headers, proxies=proxies)

    except:
        print("Sensor probably not connected")

    time.sleep(300)
