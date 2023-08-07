from dataclasses import dataclass
from restaurants import foodandco
from restaurants import restaurants


@dataclass
class Raitti:
    name = "Raitti"
    icon = ":motorway:"
    url: str = foodandco.get_url("seinajoki", "raitti")

    def getList(self) -> list[str]:
        return foodandco.getMenu('3530', False)


def initialize() -> None:
    restaurants.register("raitti", Raitti)
