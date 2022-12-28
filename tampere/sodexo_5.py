from restaurants import sodexo, restaurants
from dataclasses import dataclass


@dataclass
class Sodexo5:
    name = "Sodexo 5"
    icon = ":five:"
    url = "https://www.sodexo.fi/ravintolat/ravintola-hermia-5"

    def getList(self) -> list[str]:
        return sodexo.getList(107)


def initialize() -> None:
    restaurants.register("sodexo_5", Sodexo5)
