from restaurants import foodandco, restaurants
from dataclasses import dataclass


@dataclass
class Fiilu:
    name = "Fiilu"
    icon = ":one:"
    url = "https://www.foodandco.fi/fiilu"

    def getList(self) -> list[str]:
        return foodandco.getMenu('3364', False)


def initialize() -> None:
    restaurants.register("fiilu", Fiilu)
