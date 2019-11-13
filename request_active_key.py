# 111319 Jinny Park
# A python script for requesting API
# Python 3.6
import requests, json #conda install request
#from aiohttp import web
header = {"Accept": "application/json", "Content-Type": "application/json", "username": "jinnyparkmus", "password": "mypassword"} #replace "mypassword" with real pw

url = 'https://api.hooktheory.com/v1/users/auth'
r = requests.post(url, data=header)
print(r.json())

# output: {'id': 012345, 'username': 'jinnyparkmus', 'email': 'youremail@gmail.com', 'activkey': 'abcdefgghjqwert1234556', 'plus': False}
