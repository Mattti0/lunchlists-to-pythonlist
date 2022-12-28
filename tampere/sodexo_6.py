from restaurants import sodexo, restaurants
from dataclasses import dataclass


@dataclass
class Sodexo6:
    name = "Sodexo 6"
    icon = ":six:"
    url = "https://www.sodexo.fi/ravintolat/tampere/hermia-6"

    def getList(self) -> list[str]:
        return sodexo.getList(110)


def initialize() -> None:
    restaurants.register("sodexo_6", Sodexo6)
