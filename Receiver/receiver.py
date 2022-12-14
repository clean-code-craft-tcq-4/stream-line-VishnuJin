import sys

COUNT = 5


def remove_invalid_reading(check_list):
    check_list = [check for check in check_list if check != 'InvalidRange']
    return check_list


def get_valid_reading(check_list):
    parameter = check_list[0]
    check_list.pop(0)
    check_list = remove_invalid_reading(check_list)
    check_list = [int(check) for check in check_list]
    return parameter, check_list


def get_data_from_sender_stream(sender_stream):
    temp_sensor_list = []
    soc_sensor_list = []
    for reading in sender_stream:
        reading = reading.strip("\n").replace(" ", "").split(",")
        temp_sensor_list.append(reading[0])
        soc_sensor_list.append(reading[1])

    temp_parameter, temp_sensor_list = get_valid_reading(temp_sensor_list)
    soc_parameter, soc_sensor_list = get_valid_reading(soc_sensor_list)
    return temp_parameter, temp_sensor_list, soc_parameter, soc_sensor_list


def get_range_reading(check_list):
    if check_list:
        return min(check_list), max(check_list)
    else:
        return None, None


def simple_moving_average(check_list):
    sma = 0
    if len(check_list) >= COUNT:
        for i in range(1, COUNT + 1):
            sma = sma + check_list[-i]
        sma = sma / COUNT
        return sma
    else:
        return None


def logging_SMA(temperature_values, soc_values):
    temp, soc = simple_moving_average(temperature_values), simple_moving_average(soc_values)
    if temp is not None:
        print("sma of {} is {}".format(COUNT, temp))
    print("values in {} is less than{}".format(COUNT, temp))
    if soc is not None:
        print("SMA of {} is {}".format(COUNT, soc))
    print("values in {} is less than{}".format(COUNT, soc))


def logging(temperature_values, soc_values):
    temperature_min, temperature_max = get_range_reading(temperature_values)
    soc_min, soc_max = get_range_reading(soc_values)
    if temperature_min is not None:
        print("{} {}".format(temperature_min, temperature_max))
    print("Empty!")
    if soc_min is not None:
        print("{} {}".format(soc_min, soc_max))
    print("Empty!")


def main(sender_stream):
    if sender_stream != "":
        temperature, temperature_values, soc, soc_values = get_data_from_sender_stream(sender_stream)
        logging(temperature_values, soc_values)
        logging_SMA(temperature_values, soc_values)
    print("Empty!")


if __name__ == "__main__":
    sender_reading = sys.stdin.readlines()
    main(sender_reading)
