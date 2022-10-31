"""
This module mimics a temperature sensor
"""


from sensors.sensor import Sensor


class Temperature(Sensor):
    def __init__(self) -> None:
        self.MIN = 0
        self.MAX = 45
        super().__init__()
