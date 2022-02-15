import requests



url = 'https://tradeappapiassistant.herokuapp.com/telegram'

status_endpoint = '/history'


req=requests.get(url+status_endpoint)
resp = req.json()
print()

