import requests

import json

url = "https://www.clubhouseapi.com/api/join_channel"

payload = "{\r\n \"channel\": \"PYQG4yqO\" , \"user_id\": 1928455578  \r\n}"

token = ['4b2dd476eeb7aeaf07ca8287f1f212bd86ff6f51', '9805ce85440526ef00c98cdaff7864f17e9ab52b', 'c43cfb7f5ecad5fcdd7ae58b1b815344c211974d',
         '09b51eeaa5ceb2f4cbdad1beb1c1783f3729ea3f', '44f2e86e2af41de274b7d46500752401b54259de', '91ace477cda07ddd7df181955ef3f04d57f185af', 'c94ac4c09c079d788e56b45ec0863b6939ecf94e',
         '69a151141d100f112fe0fb7ad530f3d718d944a6', '41703491f8f1eeaeead02975ee51cde78cd01bf6', '225ceec4dcfcdbc7da8cb010a1dd3cc8927c0a6d', '0fc93c6db2ed7d1a8963922c8809f0cb5c2bb15e',
         '73150a3a12ad0943e779f9af5ee6239ec58ce782', 'ad02fbde5e483405ccaa9df437dd259c908f20ac', 'f17022af1e9290bd00f6e5d44c96747d6d9d9b46', '756a801863de5eacfc8aa669959456dee9958070',
         'b3f3329c075f5011ae3f8d56a2a1c5fd51e16aa0', '8355d97efe83565251c0c43b13653877b22b3958', '226e09c529fc38f8de82b4d77706ddf6c35c34c3',
         '4bed603674ecfa9c24d4c521b1a05a6965e18a11', 'c14e2054aa7a0a12f3ba4073156e38df4ba997cf', 'b1d289d677eaaddd832f02c253fd83fd5d02867b',
         '1087d8512f6727cd5d2219bb0c945b71263cad2c', '535357cbe78e8cdf27da746dff3e53d3214ac938', 'ad24b0909ede45ba553191d6799b49c81c58ef98',
         '9c5427eb23eccf1f9441dda5ec54e1ef5581413a', '1eb25ea4ced4f77dfd20ff33368933b116708be7', 'b7a6e806de4093922324560f05de31f407bced59',
         'e56c3ea62e9ea546a61e317ecef0f98e18c21fb2', 'acad5b3564402f75100b03eb95e34ade871fcb53', 'b8a84ab1a5919d799f4f821ce52e63d1a8ac5c4f',
         'f9a5905ad39bbf35248e3bf8c57c2919475b6dd6', '13eb19a4186410d12be27474c4e3e1c76a062a15', '5a6879df13422ad5fe83b3fb0b7ee30d000d686a'
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
