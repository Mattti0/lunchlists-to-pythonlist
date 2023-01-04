from dataclasses import dataclass
from restaurants import foodandco
from restaurants import restaurants


@dataclass
class Areena:
    name = "Areena"
    icon = ":stadium:"
    url: str = foodandco.get_url("seinajoki", "areena")

    def getList(self) -> list[str]:
        return foodandco.getMenu('3533', False)


def initialize() -> None:
    restaurants.register("areena", Areena)
