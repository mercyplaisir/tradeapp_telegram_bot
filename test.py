import requests
import json
# res = requests.get('http://localhost:5000/telegram/status').json()
r = json.dumps("on")
n=json.loads(r)


print(n)