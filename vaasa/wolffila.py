from datetime import datetime, date
from dataclasses import dataclass
import requests
import json
import re
from restaurants import foodandco

from restaurants import restaurants


@dataclass
class Wolffila:
    name: str = "Wolffila"
    icon: str = ":wolf:"
    url: str = foodandco.get_url("vaasa", "wolffila")

    def getList(self) -> list[str]:
        menu = []
        # Workaround as Wolffila's normal foodandco JSON is often empty
        list_url = 'https://www.compass-group.fi/menuapi/week-menus?costCenter=0253&date=#date#&language=fi'
        wolf_list = requests.get(list_url.replace(
            "#date#", date.today().isoformat())).json()

        day_menu = wolf_list['menus'][datetime.today().weekday()]['html'].replace(
            '<p>', '').replace('</p>', '')
        day_menu = day_menu.split('<br />')
        for i in day_menu:
            text = i
            text = re.sub(r'[0-9]+\,?[0-9]*$', '', text).strip()
            menu.append(text)

        return menu


def initialize() -> None:
    restaurants.register("wolffila", Wolffila)
