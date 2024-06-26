#Package


#Libraries
import urllib.parse
import pandas as pd
import requests

#Use your API credentials
apiKey= "pass_your_key"
secretKey = "pass_your_secretkey"
rurl = urllib.parse.quote('https://127.0.0.1:5000/', safe = "")

uri = f'https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={apiKey}&redirect_uri={rurl}'

url = 'https://api-v2.upstox.com/login/authorization/token'
code = 'U8HB1v'
headers = {
    'accept': 'application/json',
    'Api-Version': '2.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'code': code,
    'client_id': apiKey,
    'client_secret': secretKey,
    'redirect_uri': "https://127.0.0.1:5000/",
    'grant_type': 'authorization_code'
}

response = requests.post(url, headers=headers, data=data)
json_response = response.json()
json_response

access_token = json_response['access_token']

import requests

def make_request(method, url, headers=None, params=None, data=None):
    response = None

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers, params=params)
        elif method == 'POST':
            response = requests.post(url, headers=headers, params=params, json=data)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, params=params, json=data)
        else:
            raise ValueError('Invalid HTTP method.')

        
        if response.status_code == 200:
           
            return response.json()
        else:
            
            return response

    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None

url = f'https://api-v2.upstox.com/historical-candle/intraday/NSE_INDEX|Nifty 50/30minute' 
headers = {
    'accept': 'application/json',
    'Api-Version': '2.0',
    
}

response = make_request('GET', url, headers=headers)
response


#Initialing Upstox Websocket
from upstox_api.api import Upstox
from upstox_api import WebSocket

upstox = Upstox('a49f3ae8-7107-452f-907d-f6469b330d4f')  # Replace '<your_api_key>' with your actual API key

# Connect to WebSocket
def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

ws = WebSocket(upstox.get_api_secret(), upstox.get_token())
ws.on_message = on_message
ws.on_error = on_error
ws.on_close = on_close


# Subscribe to Nifty 50
ws.subscribe(['nse_index/NIFTY 50'], nse_index=True)

# Start WebSocket
ws.run_forever()
