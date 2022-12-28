""""Restaurant protocol


Use this also as a template for new restaurant Plugin.

1. import restaurants 
2. implement getList & initialize
3. remove relations to Protocol
4. fill class details
5. add new plugin to config.toml under related city

"""

#from restaurants import restaurants
from dataclasses import dataclass
from typing import Protocol


@dataclass
class Restaurant(Protocol):
    name: str
    icon: str
    url: str

    def getList(self) -> list[str]:
        """Every restaurant object should return list"""

# def initialize() -> None:
#   restaurants.register("pluginNameInConfig", pluginClass)
