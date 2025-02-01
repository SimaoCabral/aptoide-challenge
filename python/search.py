import base64
import requests
import json

from utils import extract_q

search_link = "https://ws75.aptoide.com/api/7/apps/get/store_name=apps/q=bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA/group_name=games/limit=10/offset=0/mature=false"

response = requests.get(search_link)

body = response.json()
print(f"Pretty response body:\n {json.dumps(body, indent=4)}")
print("----------------------------")
item_list = body['datalist']
c=1
for item in item_list['list']:
    print(f"App {c}-> {item['name']}")
    c+=1
print("----------------------------")
q = extract_q(search_link)
print(f"Original q value: {q}")
print(f"Base64 decoded q: {base64.b64decode(q).decode('utf-8')}")


