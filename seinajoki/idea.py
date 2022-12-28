from restaurants import juvenes, restaurants
from dataclasses import dataclass


@dataclass
class Idea:
    name = "Idea"
    icon = ":heavy_exclamation_mark:"
    url = "http://www.juvenes.fi/idea"

    def getList(self) -> list[str]:
        menu = juvenes.GetMenuJamix('93077', '2')
        menu += juvenes.GetExceptions(4159)

        return menu


def initialize() -> None:
    restaurants.register("idea", Idea)
