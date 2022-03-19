import requests

import json

url = "https://www.clubhouseapi.com/api/join_channel"

payload = "{\r\n \"channel\": \"PYQG4yqO\" , \"user_id\": 1928455578  \r\n}"

token = ['4b2dd476eeb7aeaf07ca8287f1f212bd86ff6f51', '9805ce85440526ef00c98cdaff7864f17e9ab52b', 'c43cfb7f5ecad5fcdd7ae58b1b815344c211974d'
         ]
for i in range(300):
    headers = {
        'CH-Languages': 'en-US',
        'CH-Locale': 'en_US',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'CH-AppBuild': '2576',
        'CH-AppVersion': '0.1.8',
        'CH-UserID': '1928455578',
        'User-Agent': 'clubhouse/2576 (iPhone; iOS 14.4; Scale/2.00)',
        'Connection': 'close',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Token '+token[i]
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
