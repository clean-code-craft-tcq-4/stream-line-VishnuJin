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


