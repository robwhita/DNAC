import requests
import json
import os
import urllib3
...
urllib3.disable_warnings()

def DNAC_auth():
    url = 	'https://sandboxdnac2.cisco.com/dna'
    auth_url = '/system/api/v1/auth/token'

    user = os.environ['USER']
    password = os.environ['PASS']

    headers = {
        'content-type': "application/json",
        }

    response = requests.post(url=f'{url}{auth_url}', auth=(user, password), verify=False, headers=headers)
    token = response.json()['Token']
    return token 

if __name__ == '__main__':
    DNAC_auth()


    



