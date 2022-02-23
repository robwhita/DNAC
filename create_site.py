import requests
import json
import urllib3
from DNAC_auth import DNAC_auth
from task_checker import task_checker
...
urllib3.disable_warnings()

def create_site(token): 
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/site'
    body = {
    "type": "area",
    "site": {
        "area": {
            "name": "Antartica1234",
            "parentName": "Global"
        }}}
    headers = {'x-auth-token': token,
    'content-type': 'application/json'}    
    response = requests.post(headers=headers, data=json.dumps(body), url=url, verify=False) 
    url_response = json.loads(response.text)
    return url_response

if __name__ == '__main__':
    token = DNAC_auth()
    url_response = create_site(token)
    task_status = task_checker(token, url_response)
    print(json.dumps(task_status, indent=2))


