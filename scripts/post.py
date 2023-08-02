import requests

URL_POST_ROOMS ='https://wmzruqeedl.execute-api.ap-southeast-2.amazonaws.com/createRoom'
headers = {}
params = {
    "name": "Created by Lambda", 
    "description":"IT WORKS!", 
    "updated": '2022-04-21 00:19:07.096118+00', 
    "created": '2022-04-21 00:19:06.096118+00', 
    "host_id": 3, 
    "topic_id": 3
    }
data = {}

def post():
    requests.request("POST", URL_POST_ROOMS, params=params)

post()