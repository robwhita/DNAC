import requests
import json
import urllib3
from DNAC_auth import DNAC_auth
from get_devices import get_devices
...
urllib3.disable_warnings()

def get_device_ID(device_name, devices):
    device_resp = devices['response']
    for device in device_resp: 
        if device['hostname'] == device_name: 
            id = device['id']
            return id 

if __name__ == '__main__':
    token = DNAC_auth()
    devices = get_devices(token)
    id = get_device_ID(device_name='leaf1.test.com', devices=devices)
    print(json.dumps(id, indent=2))


