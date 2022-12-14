from restaurants import foodandco, restaurants
from dataclasses import dataclass


@dataclass
class Smarthouse:
    name = "Smarthouse"
    icon = ":space_invader:"
    url: str = foodandco.get_url("oulu", "smarthouse")

    def getList(self) -> list[str]:
        return foodandco.getMenu('3498', False)


def initialize() -> None:
    restaurants.register("smarthouse", Smarthouse)
