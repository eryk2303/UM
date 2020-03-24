import Mesure


def find_split(training_data):
    best_gain_value = 0
    best_question_split = None

    for column in range(len(training_data[0]) - 1):
        value =  set([data[column] for data in training_data])
        for unique_value in value:

            question_split = column, unique_value

            true_data, false_data = [], []

            for data in training_data:

                if isinstance(question_split[1], int) or isinstance(question_split[1], float):
                    if (question_split[1] <= data[column]):
                        true_data.append(data)
                    else:
                        false_data.append(data)
                else:
                    if (question_split[1] == data[column]):
                        true_data.append(data)
                    else:
                        false_data.append(data)

            if len(true_data) == 0 or len(false_data) == 0:
                continue
            gain = Mesure.gain(true_data, false_data, training_data)

            if gain >= best_gain_value:
                best_gain_value = gain
                best_question_split = question_split


    return best_gain_value, best_question_split


training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 10, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 30, 'Lemon'],
]

find_split(training_data)
