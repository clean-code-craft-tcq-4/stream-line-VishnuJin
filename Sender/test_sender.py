import io
import json
from unittest.mock import patch



from sender import read_data_from_sensors, send_readings
from sensors.battery_temperature import Temperature
from sensors.state_of_charge import StateOfCharge


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


def test_send_readings():
    with patch('sys.stdout', new=io.StringIO()) as stdout:
        send_readings(1)
    output = json.loads(stdout.getvalue())
    assert type(output) == dict