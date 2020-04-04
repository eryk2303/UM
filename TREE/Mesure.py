def count(training_elements):
    count_data = {}
    for count in training_elements:
        tmp = count[-1]

        if tmp not in count_data:
            count_data[tmp] = 0
        count_data[tmp] += 1
    return count_data


def giny(training_data):
    quantity = count(training_data)
    giny_tmp = 0
    for elements in quantity:
        giny_tmp += (quantity[elements] / len(training_data)) ** 2

    return 1 - giny_tmp


def gain(false, true, current):
    help_value = float(len(false)) / (len(false) * len(true))
    info_gain = giny(current) - help_value * giny(false) - (1 - help_value) * giny(true)
    return info_gain
