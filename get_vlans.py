import requests
import json
import urllib3
from DNAC_auth import DNAC_auth
from get_devices import get_devices
from get_device_ID import get_device_ID
...
urllib3.disable_warnings()

def get_vlans(id):
    url = f'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device/{id}/vlan'
    headers = {'x-auth-token': token,
    'content-type': 'application/json'} 
    id = requests.get(url=url, headers=headers, verify=False).json() 
    return id 

if __name__ == '__main__':
    token = DNAC_auth()
    devices = get_devices(token)
    id = get_device_ID(device_name='leaf2.test.com', devices=devices)
    vlans = get_vlans(id)
    print(json.dumps(vlans, indent=2))


    