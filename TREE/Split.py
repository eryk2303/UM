import Mesure


##function to find the best split
# @param training_elements list in which items will be split
# @return best_gain_value the best find gain 
# @return best_question_split the best find question to split
# @return best_true_data the best find list with true data
# @return best_false_data the best find list with false data
def make_split(training_data):
    best_gain_value = 0
    best_question_split = None
    best_true_data, best_false_data = [], []

    for column in range(len(training_data[0]) - 1):
        ##set with questions to share
        value = set([data[column] for data in training_data])

        for unique_value in value:

            question_split = column, unique_value

            true_data, false_data = [], []

            ## dividing data according to the selected query
            for data in training_data:
                if isinstance(question_split[1], int) or isinstance(question_split[1], float):
                    if question_split[1] <= data[question_split[0]]:
                        true_data.append(data)
                    else:
                        false_data.append(data)
                else:
                    if question_split[1] == data[question_split[0]]:
                        true_data.append(data)
                    else:
                        false_data.append(data)

            if len(true_data) == 0 or len(false_data) == 0:
                continue
            gain = Mesure.gain(true_data, false_data, training_data)
            ##save the best data
            if gain >= best_gain_value:
                best_gain_value = gain
                best_question_split = question_split
                best_false_data = false_data
                best_true_data = true_data

    return best_gain_value, best_question_split, best_true_data, best_false_data


##function to do split for only one question 
# @param training_elements list in which items will be split
# @return best_gain_value the best find gain 
# @return best_question_split the best find question to split
# @return best_true_data the best find list with true data
# @return best_false_data the best find list with false data
def check_split(training_data, question_split):
    true_data, false_data = [], []

    for data in training_data:
        if isinstance(question_split[1], int) or isinstance(question_split[1], float):
            if question_split[1] <= data[question_split[0]]:
                true_data.append(data)
            else:
                false_data.append(data)
        else:
            if question_split[1] == data[question_split[0]]:
                true_data.append(data)
            else:
                false_data.append(data)

    if len(true_data) is not 0 and len(false_data) is not 0:
        gain = Mesure.gain(true_data, false_data, training_data)
    else:
        gain = 0

    return gain, question_split, true_data, false_data
