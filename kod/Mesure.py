__author__ = '{Eryk Wawrzyn}'


##function to count elements in all attributes
# @param training_elements list in which items will be counted
# @return count_data dictionary with quantity of elements in all category
def count(training_elements):
    count_data = {}
    for count in training_elements:
        tmp = count[-1]

        if tmp not in count_data:
            count_data[tmp] = 0
        count_data[tmp] += 1
    return count_data


##function to calculate the gini coefficient
# @param training_elements list in which items will be counted
# @return 1 - giny_tmp gini coefficient
def giny(training_data):
    quantity = count(training_data)
    giny_tmp = 0
    for elements in quantity:
        giny_tmp += (quantity[elements] / len(training_data)) ** 2

    return 1 - giny_tmp


##function to calculate the information gain
# @param false list of false elements in which the information gain will be counted
# @param true list of true elements in which the information gain will be counted
# @param current all list of true elements in which the information gain will be counted
# @return info_gain information gain for current split
def gain(false, true, current):
    help_value = float(len(false)) / (len(false) * len(true))
    info_gain = giny(current) - help_value * giny(false) - (1 - help_value) * giny(true)
    return info_gain
