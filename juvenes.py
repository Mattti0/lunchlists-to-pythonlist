#!/usr/bin/python
# -*-coding:utf-8 -*-
from datetime import datetime, date
import requests
import json
from bs4 import BeautifulSoup as soup
import re

# Juvenes API parser


def GetMenuJamix(CustomerId, RestaurantId):
    menu = []
    apiUrl = "http://fi.jamix.cloud/apps/menuservice/rest/haku/menu/#customerId#/#restaurantId#"
    apiUrl = apiUrl.replace("#customerId#", CustomerId).replace(
        "#restaurantId#", RestaurantId)
    requestInfo = {'type': json, 'date': date.today(
    ).isoformat().replace('-', ''), 'lang': 'fi'}
    response = requests.get(apiUrl, params=requestInfo)
    menuJson = response.json()

    if (len(menuJson) > 0):
        for menutype in menuJson[0]['menuTypes']:
            for meal in menutype['menus'][0]['days'][0]['mealoptions']:
                if meal['name'].encode('utf-8') == 'JÄLKIRUOKA':
                    continue
                for item in meal['menuItems']:
                    itemName = item['name']

                    if len(item['diets']) > 0:
                        itemName += " (" + item['diets'] + ")"

                    if itemName not in menu:
                        menu.append(itemName)
    return menu


def GetExceptions(RestaurantId):
    exceptions = []
    todayDate = datetime.today()
    apiUrl = "https://www.juvenes.fi/DesktopModules/Talents.Restaurants/RestaurantsService.svc/GetRestaurant"
    requestInfo = {'restaurantId': RestaurantId, 'lang': 'fi'}

    try:
        jsonResponse = requests.get(apiUrl, params=requestInfo).json()
        startTemplate = 'Exeption?Start'
        endTemplate = 'Exeption?End'
        infoTitleTemplate = 'Exeption?InfoTitle'
        infoTextTemplate = 'Exeption?InfoText'

        for exepId in range(1, 3):
            exeptionStart = re.search(
                r'[0-9]\d+', jsonResponse['d']['OpenInfo'][startTemplate.replace('?', str(exepId))]).group()
            exeptionEnd = re.search(
                r'[0-9]\d+', jsonResponse['d']['OpenInfo'][endTemplate.replace('?', str(exepId))]).group()

            exStartDate = datetime.fromtimestamp(float(exeptionStart)/1000)
            exEndDate = datetime.fromtimestamp(float(exeptionEnd)/1000)

            if (exEndDate.day == todayDate.day and exEndDate.month == todayDate.month) \
                    or (exStartDate.day == todayDate.day and exStartDate.month == todayDate.month) \
                    or (todayDate <= exEndDate and todayDate >= exStartDate):
                warningString = ":warning: "
                warningString += jsonResponse['d']['OpenInfo'][infoTitleTemplate.replace(
                    '?', str(exepId))].rstrip()
                if len(warningString) > 9 and jsonResponse['d']['OpenInfo'][infoTextTemplate.replace('?', str(exepId))]:
                    warningString += ", "
                warningString += jsonResponse['d']['OpenInfo'][infoTextTemplate.replace(
                    '?', str(exepId))]
                exceptions.append("#BOLD#" + warningString + "#BOLD#")
    except:
        pass

    return exceptions


if __name__ == "__main__":
    exit(0)
