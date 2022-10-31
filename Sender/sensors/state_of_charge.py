"""
This module mimics a StateOfCharge sensor
"""


from sensors.sensor import Sensor


class StateOfCharge(Sensor):
    def __init__(self) -> None:
        self.MIN = 20
        self.MAX = 80
        super().__init__()
