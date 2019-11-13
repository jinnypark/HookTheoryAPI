# 111319 Jinny Park
# python script accessing Hook Theory API once active key is acquired
# Python 3.6
import requests, json

header = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer ***********"}  #replace ******** with active key value
url = 'https://api.hooktheory.com/v1/trends/nodes'
#see https://www.hooktheory.com/api/trends/docs for more paths
r = requests.get(url, data=header, headers = header)
print(r.status_code)
print(r.json())
