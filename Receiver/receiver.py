import os
import sys
import json
from typing import Tuple

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Sender.sender import max_readings_per_stream
from Receiver.compute_statistics import calculate_statistics


def print_stats(data: list, writer:callable=print):
    """
    prints the statistics to the console.
    Also accepts the second argument `writer` which should be a function
    the calculated statistics data will be forwarded to the `writer` function
    """
    writer("\n".join(calculate_statistics(data)))


def convert_to_json(data:str)->Tuple[ValueError|None, dict|None]:
    """
    converts the given str to data and return along with err value
    """
    try:
        return None, json.loads(data)
    except:
        return ValueError("Invalid JSON format"), None


def input_collector(input_count:int)->list:
    """
        collects the inputs by iterating the given number of times and returns it as list
    """
    data = []
    for _ in range(input_count):
        datum = input().strip()
        if len(datum) > 0:
            err, json_value = convert_to_json(datum)
            if err:
                raise err
            data.append(json_value)
    return data


if __name__ == "__main__":
    data = input_collector(max_readings_per_stream)
    print(f"Data From Sender..")
    print(data)

    print()
    print(f"Data From Receiver..")
    print_stats(data)
