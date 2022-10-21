"""Base Template for Sensors"""
import random


class Sensor:
    def fetch_reading(self):
        reading = random.randint(self.MIN, self.MAX)
        return (
            reading
            if self.is_reading_valid(reading)
            else ValueError("Invalid data from Sensor")
        )

    def is_reading_valid(self, reading):
        return (reading <= self.MAX) and (reading >= self.MIN)
