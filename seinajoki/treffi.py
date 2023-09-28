from dataclasses import dataclass
from restaurants import foodandco
from restaurants import restaurants


@dataclass
class Treffi:
    name = "The Local Cafe Treffi"
    icon = ":coffee:"
    url: str = foodandco.get_url("seinajoki", "the-local-cafe-treffi")

    def getList(self) -> list[str]:
        return foodandco.getMenu('353001', False)


def initialize() -> None:
    restaurants.register("treffi", Treffi)
