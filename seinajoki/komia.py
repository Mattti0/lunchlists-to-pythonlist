from restaurants import juvenes, restaurants
from dataclasses import dataclass


@dataclass
class Komia:
    name = "Komia"
    icon = ":diamonds:"
    url = "http://www.juvenes.fi/komia"

    def getList(self) -> list[str]:
        menu = juvenes.GetMenuJamix('93077', '43')
        menu += juvenes.GetExceptions(4158)

        return menu


def initialize() -> None:
    restaurants.register("komia", Komia)
