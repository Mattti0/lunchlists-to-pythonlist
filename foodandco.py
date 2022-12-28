import requests

def endpoint(id) -> str:
    return f"https://www.compass-group.fi/menuapi/feed/json?costNumber={id}&language=fi"


def getMenu(restaurantId, variablePricing):
    menu = []
    list_url = endpoint(restaurantId)
    menujson = requests.get(list_url).json()

    if (len(menujson['MenusForDays']) == 0):
        menu.append("List is empty")
        return menu

    day_menu = menujson['MenusForDays'][0]['SetMenus']

    for i in day_menu:
        if (len(i['Components']) > 0):
            if (variablePricing):
                menu.append("{} ({} €)".format(i['Name'], i['Price']))
            else:
                if i['Name'] == None:
                    menu.append('Lounas')
                else:
                    menu.append(i['Name'])

            for c in i['Components']:
                item = "\\t{}".format(c)
                if item not in menu:
                    menu.append(item)

    return menu
