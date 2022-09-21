from sender import read_data_from_sensors, send_readings
from sensors.battery_temperature import Temperature
from sensors.state_of_charge import StateOfCharge
import json
import os


def test_read_data_from_sensors():
    sensors = {"Temperature": Temperature, "SOC": StateOfCharge}
    actual_result = read_data_from_sensors(sensors)
    assert "Temperature", "SOC" in actual_result.keys()


def test_read_data_from_sensors_is_valid():
    sensors = {"Temperature": Temperature, "SOC": StateOfCharge}
    actual_result = read_data_from_sensors(sensors)
    assert Temperature().is_reading_valid(
        actual_result["Temperature"]
    ) and StateOfCharge().is_reading_valid(actual_result["SOC"])


def write_to_file(json_reading):
    with open("readings.json", "w") as outfile:
        outfile.write(json_reading)


def test_send_readings():
    readings_file = "readings.json"
    send_readings(write_to_file)
    with open(readings_file, "r") as outfile:
        json_readings = json.load(outfile)
    os.remove(readings_file)
    assert len(json_readings) == 50
