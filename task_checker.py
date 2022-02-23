import requests
import json
import urllib3

...
urllib3.disable_warnings()

def task_checker(token, url_response):
    StatusURL = url_response['executionStatusUrl']
    url = f'https://sandboxdnac2.cisco.com{StatusURL}'
    headers = {'x-auth-token': token,
    'content-type': 'application/json'} 
    task_status = requests.get(url=url, headers=headers, verify=False).json()
    while task_status['status'] == 'IN_PROGRESS': 
        task_status = requests.get(url=url, headers=headers, verify=False).json()
    return task_status


