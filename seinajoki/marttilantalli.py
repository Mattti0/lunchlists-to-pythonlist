from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup as soup
from datetime import datetime

from restaurants import restaurants


@dataclass
class MarttilanTalli:
    name: str = "Marttilan Talli"
    icon: str = ":horse:"
    url: str = "https://www.marttilantalli.fi/lounas-seinajoki/"

    def getList(self) -> list[str]:
        list_url = 'https://www.lounaat.info/lounas/marttilan-talli/seinajoki'

        response = requests.get(list_url)
        lunchmenu = soup(response.content, 'html.parser').find(
            'div', attrs={'id': 'menu'}).findAll('div', attrs={'class': 'item-body'})

        lunchmenu = list(map(lambda x: x.findAll('p'), lunchmenu))
        lunchmenu = [list(map(lambda x: x.get_text().strip(), l))
                     for l in lunchmenu]
        lunchmenu = lunchmenu[datetime.today().weekday()]
        # remove extra spaces from strings
        menu = [" ".join(l.split()) for l in lunchmenu]
        return menu


def initialize() -> None:
    restaurants.register("marttilantalli", MarttilanTalli)
