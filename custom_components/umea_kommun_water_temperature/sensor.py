"""Platform for sensor integration."""
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity

from py_umea_kommun_water_temperature import *


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([ BettnessandWaterTemperature()
                 , BolesholmarnaWaterTemperature()
                 , KarleksvikenWaterTemperature()
                 , LankeboWaterTemperature()
                 , LjumvikenWaterTemperature()
                 , StocksjonWaterTemperature()
                 , NydalabadetWaterTemperature()
                 ])


class WaterTemperature(Entity):
    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return TEMP_CELSIUS


class BettnessandWaterTemperature(WaterTemperature):
    @property
    def name(self):
        return "Bettnessand"

    def update(self):
        self._state = get_bettnessand()


class BolesholmarnaWaterTemperature(WaterTemperature):
    @property
    def name(self):
        return "Bölesholmarna"

    def update(self):
        self._state = get_bolesholmarna()


class KarleksvikenWaterTemperature(WaterTemperature):
    @property
    def name(self):
        return "Kärleksviken"

    def update(self):
        self._state = get_karleksviken()


class LankeboWaterTemperature(WaterTemperature):
    @property
    def name(self):
        return "Länkebo"

    def update(self):
        self._state = get_lankebo()


class LjumvikenWaterTemperature(WaterTemperature):
    @property
    def name(self):
        return "Ljumviken"

    def update(self):
        self._state = get_ljumviken()


class StocksjonWaterTemperature(WaterTemperature):
    @property
    def name(self):
        return "Stöcksjön"

    def update(self):
        self._state = get_stocksjon()


class NydalabadetWaterTemperature(WaterTemperature):
    @property
    def name(self):
        return "Nydalabadet"

    def update(self):
        self._state = get_nydalabadet()
