import json
from sensors.battery_temperature import Temperature
from sensors.state_of_charge import StateOfCharge

max_readings_per_stream = 50

sensors = {"Temperature": Temperature, "StateOfCharge": StateOfCharge}


def read_data_from_sensors(sensors):
    readings = {}
    for battery_parameter_type in sensors.keys():
        readings[battery_parameter_type] = sensors[
            battery_parameter_type
        ]().fetch_reading()

    return readings


def get_readings_as_json_dump(readings):
    return json.dumps(readings)


def send_readings(writer=print):
    writer(
        get_readings_as_json_dump(
            [read_data_from_sensors(sensors) for _ in range(max_readings_per_stream)]
        )
    )


if __name__ == "__main__":
    send_readings()
