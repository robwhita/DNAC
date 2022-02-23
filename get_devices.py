import requests
import json
import urllib3
from DNAC_auth import DNAC_auth
...
urllib3.disable_warnings()

def get_devices(token):
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device' 
    headers = {'x-auth-token': token,
    'content-type': 'application/json'} 
    devices = requests.get(url=url, headers=headers, verify=False).json() 
    return devices 

if __name__ == '__main__':
    token = DNAC_auth()
    devices = get_devices(token)
    print(json.dumps(devices, indent=2))