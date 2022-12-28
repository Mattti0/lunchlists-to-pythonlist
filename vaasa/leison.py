from urllib import request as urllib
from bs4 import BeautifulSoup as soup
from datetime import datetime
from restaurants import restaurants
from dataclasses import dataclass


@dataclass
class Leison:
    name = "Leison"
    icon = ":black_joker:"
    url = "www.leisoncafe.fi"

    def getList(self) -> list[str]:
        menu = []

        list_url = 'http://www.leisoncafe.fi/?page=Leison+Cafe&setlang=l2'
        site = urllib.urlopen(list_url).read()
        lunch_data = soup(site, 'html.parser').find(
            'div', attrs={'id': 'lunch-menu-list'})
        items = lunch_data.findAll(
            'table')[datetime.today().weekday()].findAll('td')

        menu = [i.get_text() for i in items]
        if len(menu) == 1:
            raise ValueError()

        return menu


def initialize() -> None:
    restaurants.register("leison", Leison)
