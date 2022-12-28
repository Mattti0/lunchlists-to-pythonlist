from urllib import request as urllib
from bs4 import BeautifulSoup as soup
from datetime import datetime, date
from restaurants import restaurants
from dataclasses import dataclass



@dataclass
class KesmoVaasa:
    name = "Kesmo Vaasa"
    icon = ":meat_on_bone:"
    url = "https://www.kesmo.fi/lounas/kesmo-vaasa/"

    WEEKDAY = datetime.today().weekday()
    WEEKDAYS_LOOKUP = ["maanantai", "tiistai",
                    "keskiviikko", "torstai", "perjantai"]

    def getList(self) -> list[str]:
        menu = []

        list_url = 'https://www.kesmo.fi/lounas/kesmo-vaasa/'
        site = urllib.urlopen(list_url).read()
        lunch_data = soup(site, 'html.parser').find(
            "div", attrs={"class": "LunchList"})

        items = lunch_data.findAll('tr')

        start_index = -1
        end_index = 0

        for i in items:
            if start_index == -1 and (self.WEEKDAYS_LOOKUP[self.WEEKDAY] in i.get_text().lower()):
                start_index = items.index(i) + 1
            elif start_index > -1 and self.WEEKDAY != 4:
                if (self.WEEKDAYS_LOOKUP[self.WEEKDAY+1] in i.get_text().lower()):
                    end_index = items.index(i)
            elif self.WEEKDAY == 4:
                end_index = len(items)

        for i in range(start_index, end_index):
            if items[i].get_text():
                menu.append(items[i].get_text().strip())

        return menu


def initialize() -> None:
    restaurants.register("kesmovaasa", KesmoVaasa)
