from dnacentersdk import DNACenterAPI
import os 
import urllib3
...
urllib3.disable_warnings()

user = os.environ['USER']
password = os.environ['PASS']

api = DNACenterAPI(username=user, password=password, base_url="https://sandboxdnac2.cisco.com", version='2.2.3.3', verify=False)

payload = {
 "type": "area",
 "site": {
  "area": {
   "name": "AREA_52",
   "parentName": "Global"
  }}}

create_site_response = api.sites.create_site(payload=payload)
print(create_site_response)
get_site_response = api.sites.get_site(name='Global/AREA_52')
print(get_site_response)



