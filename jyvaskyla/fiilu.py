from restaurants import foodandco, restaurants
from dataclasses import dataclass


@dataclass
class Fiilu:
    name = "Fiilu"
    icon = ":one:"
    url: str = foodandco.get_url("jyvaskyla", "fiilu")

    def getList(self) -> list[str]:
        return foodandco.getMenu('3364', False)


def initialize() -> None:
    restaurants.register("fiilu", Fiilu)
