import requests
import json

URL_GET_ROOMS ='https://wmzruqeedl.execute-api.ap-southeast-2.amazonaws.com/getRooms'
headers = {}
params = {"query":""}
data = {}

def get():
    rooms = requests.request("GET", URL_GET_ROOMS, params=params)
    print(rooms.text)
    return json.dumps(rooms, indent=4, sort_keys=True, default=str)

get()

  