

from sensors.battery_temperature import Temperature
from sensors.state_of_charge import StateOfCharge


def test_is_temperature_reading_valid():
    assert Temperature().is_reading_valid(40) == True


def test_is_soc_valid():
    assert StateOfCharge().is_reading_valid(79) == True


def test_is_temperature_reading_invalid():
    assert Temperature().is_reading_valid(50) == False


def test_is_soc_invalid():
    assert StateOfCharge().is_reading_valid(81) == False
