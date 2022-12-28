from urllib import request as urllib
from bs4 import BeautifulSoup as soup
from datetime import datetime
from restaurants import restaurants
from dataclasses import dataclass


@dataclass
class Svenska:
    name = "Svenska Klubben"
    icon = ":crown:"
    url = "https://www.lounastauko.fi/ravintola/restaurant_bacchus"

    def getList(self) -> list[str]:
        menu = []

        list_url = 'http://www.lounastauko.fi/ravintola/restaurant_bacchus'
        site = urllib.urlopen(list_url).read()
        lunch_data = soup(site, 'html.parser').select(
            '.week-lunchlists .lunchlist')[datetime.today().weekday()]
        blocks = lunch_data.select('.lunch-block')

        for block in blocks:
            items = block.select('.lunch-items .item .item-name')
            item = ', '.join(name.get_text() for name in items).strip()
            if 'Salaattipöytä' in item or 'Lounasvaihtoehto' in item or 'Seisova lounaspöytä' in item:
                continue

            menu.append(item.replace("&", "-"))

        return menu


def initialize() -> None:
    restaurants.register("svenskaklubben", Svenska)
