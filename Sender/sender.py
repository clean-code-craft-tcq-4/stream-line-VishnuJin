import json


from Sender.sensors.battery_temperature import Temperature
from sensors.state_of_charge import StateOfCharge

max_readings_per_stream = 50

sensors = {"Temperature": Temperature, "StateOfCharge": StateOfCharge}


def read_data_from_sensors(sensors:dict)-> dict:
    """
    calls :func:`~Sender.sensors.sensor.Sensor.fetch_reading` function to read the data from the sensors and returns the data as dict
    for successful reading, a sensor should typically implement the :class:`~Sender.sensors.sensor.Sensor` interface
    """
    readings = {}
    for battery_parameter_type in sensors.keys():
        readings[battery_parameter_type] = sensors[
            battery_parameter_type
        ]().fetch_reading()

    return readings


def get_readings_as_json_dump(readings:list)-> str:
    """
    converts the json data to str and returns it.
    """
    return json.dumps(readings)


def send_readings(readings_count, writer:callable=print):
    """
    prints the reading to the console
    writer accepts a function to which the readings will be redirected.
    """
    for _ in range(readings_count):
        writer(get_readings_as_json_dump(read_data_from_sensors(sensors)))


if __name__ == "__main__":
    send_readings(max_readings_per_stream)
