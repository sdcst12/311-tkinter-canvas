import requests
import json

req = requests.get('https://api.open-meteo.com/v1/forecast?latitude=36.63&longitude=-85.88&hourly=temperature_2m')
data = req.text
fullDict = json.loads(data)