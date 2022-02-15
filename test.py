import requests



url = 'https://tradeappapiassistant.herokuapp.com/telegram'

status_endpoint = '/telegram/history'


req=requests.get(url+status_endpoint)

print(req.json())

