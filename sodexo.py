import requests
import json
from datetime import date

def getList(restaurantId):
	list_url = 'https://www.sodexo.fi/ruokalistat/output/daily_json/{}/{}'.format(str(restaurantId), date.today().isoformat())
	menujson = requests.get(list_url).json()

	return [menujson.get('courses').get(option).get('title_fi') for option in menujson['courses'].keys()]