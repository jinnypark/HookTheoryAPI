# 111319 Jinny Park
# A python script for requesting API
# Python 3.6
import requests, json #conda install request
header = {"Accept": "application/json", "Content-Type": "application/json", "username": "myid", "password": "mypassword"} 
#replace "myid" and "mypassword" with your own

url = 'https://api.hooktheory.com/v1/users/auth'
r = requests.post(url, data=header)
print(r.json())

# output: {'id': 012345, 'username': 'yourid', 'email': 'youremail@gmail.com', 'activkey': 'abcdefgghjqwert1234556', 'plus': False}
# use 'activekey' value to access data
