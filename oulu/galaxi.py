from restaurants import sodexo, restaurants
from dataclasses import dataclass


@dataclass
class Galaxi:
    name = "Galaxi"
    icon = ":ringed_planet:"
    url = "https://www.sodexo.fi/ravintolat/ravintola-galaksi"

    def getList(self) -> list[str]:
        return sodexo.getList(121)


def initialize() -> None:
    restaurants.register("galaxi", Galaxi)
