import requests

search_link = "https://ws75.aptoide.com/api/7/app/get/store_name=apps/q=bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA/package_name=com.fun.lastwar.gp/language=pt_PT/"

response = requests.get(search_link)
body = response.json()
description = body['nodes']['meta']['data']['media']['description']
print(description)
