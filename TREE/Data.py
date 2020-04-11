import csv
import pandas as pd
from sklearn.preprocessing import scale

test_len = 0.2
training_len = 0.8

##upload data
with open('bank.csv') as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=';')
    data = pd.DataFrame(list(readCSV))
    tmp = data['y']
    del data['y']
    data['balance'] = scale(data['balance'])
    data['duration'] = scale(data['duration'])
    data['pdays'] = scale(data['pdays'])
    data['campaign'] = scale(data['campaign'])
    data['previous'] = scale(data['previous'])
    data['day'] = scale(data['day'])
    data['age'] = scale(data['age'])
    data = pd.get_dummies(data=data, drop_first=True)
    data['y'] = tmp
    data_len = len(data) - 1
    data_test = (data[0:int(data_len * test_len)]).values.tolist()
    data_test_len = len(data_test)
    data_len -= data_test_len


def first_training(quantity):
    quantyty_training = int(quantity * data_len) + data_test_len
    data_training = data[data_test_len:quantyty_training]
    return data_training.values.tolist()


##data for secound trainnig
# @return data_training data to training
# @return data_test data to test
def secound_training(quantity, quantity_previous):
    quantyty_first = int(quantity_previous * data_len) + data_test_len
    quantyty_training = quantyty_first + int(quantity * data_len * training_len) + data_test_len
    data_training = data[quantyty_first:quantyty_training]
    return data_training.values.tolist()


##data for third trainnig
# @return data_training data to training
# @return data_test data to test
def third_training(quantity, quantity_previous):
    quantyty_first = int(quantity_previous * data_len) + data_test_len
    quantyty_training = quantyty_first + int(quantity * data_len * training_len) + data_test_len
    data_training = data[quantyty_first:quantyty_training]
    return data_training.values.tolist()

