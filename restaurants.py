from functools import cache
from typing import Callable
from restaurants.restaurant import Restaurant
import importlib


""""Restaurant plugins related part"""
listOfRestaurants: dict[str, Restaurant] = {}
initFunctionsForPlugins: dict[str, Callable[..., Restaurant]] = {}


class PluginInterface:
    @staticmethod
    def initialize() -> None:
        """Initialize plugin"""


def register(restaurantName: str, restaurantInit: Callable[..., Restaurant]) -> None:
    initFunctionsForPlugins[restaurantName] = restaurantInit


def importModule(name: str) -> PluginInterface:
    return importlib.import_module(name)


def importRestaurantPlugins(plugins: dict[str, dict[str, list[str]]]) -> None:
    """Load the plugins"""
    for city in plugins:
        for resName in plugins.get(city).get("restaurants"):
            try:
                plugin = importModule(f"restaurants.{city}.{resName}")
                plugin.initialize()
            except ModuleNotFoundError:
                raise ValueError(f"Couldn't find Plugin for {resName}")

    for item in initFunctionsForPlugins:
        initItem = initFunctionsForPlugins[item]
        listOfRestaurants[item] = initItem()

"""Methods to get restaurant attributes"""
@cache
def restaurantAvailable(restaurant: str) -> bool:
    return restaurant in getAllRestaurants()


def getNameForRestaurant(restaurant: str) -> str:
    if restaurantAvailable(restaurant) == False:
        raise KeyError("Restaurant not found")

    return listOfRestaurants[restaurant].name


def getIconForRestaurant(restaurant: str) -> str:
    if restaurantAvailable(restaurant) == False:
        raise KeyError("Restaurant not found")

    return listOfRestaurants[restaurant].icon


def getURLForRestaurant(restaurant: str) -> str:
    if restaurantAvailable(restaurant) == False:
        raise KeyError("Restaurant not found")

    return listOfRestaurants[restaurant].url


"""Methods to get lists for restaurants"""


def getAllRestaurants() -> list[str]:
    return list(listOfRestaurants.keys())


@cache
def getListForRestaurant(restaurant) -> list[str]:
    return listOfRestaurants[restaurant].getList()
