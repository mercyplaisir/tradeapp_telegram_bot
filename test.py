"""Just for testing some tools"""
import requests



URL = 'https://tradeappapiassistant.herokuapp.com/telegram'
STATUS_ENDPOINT = '/history'

req=requests.get(URL+STATUS_ENDPOINT)
resp = req.json()
print()
