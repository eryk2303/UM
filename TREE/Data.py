import csv
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import scale

with open('bank.csv') as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=',')
    data = pd.DataFrame(list(readCSV))

    '''data['balance'] = scale(data['balance'])
    data['duration'] = scale(data['duration'])
    data['pdays'] = scale(data['pdays'])
    data['campaign'] = scale(data['campaign'])
    data['previous'] = scale(data['previous'])
    data['day'] = scale(data['day'])
    data['age'] = scale(data['age'])
    data = pd.get_dummies(data=data, drop_first=True)'''


def first_training():
    quantyty_training = int(0.5 * 4520 * 0.8)
    data_training = data[:quantyty_training]
    quantyty_test = int(0.5 * 4520 * 0.2)
    data_test = data[quantyty_training:quantyty_test + quantyty_training]
    return data_training.values.tolist(), data_test.values.tolist()


def secound_training():
    quantyty_firs = int(0.5 * 4520)
    quantyty_training = quantyty_firs + int(0.25 * 4520 * 0.8)
    data_training = data[quantyty_firs:quantyty_training]
    quantyty_test = int(0.25 * 4520 * 0.2)
    data_test = data[quantyty_training:quantyty_test + quantyty_training]
    return data_training.values.tolist(), data_test.values.tolist()

def third_training():
    quantyty_firs = int(0.75 * 4520)
    quantyty_training = quantyty_firs + int(0.25 * 4520 * 0.8)
    data_training = data[quantyty_firs:quantyty_training]
    quantyty_test = int(0.25 * 4520 * 0.2)
    data_test = data[quantyty_training:quantyty_test + quantyty_training]
    return data_training.values.tolist(), data_test.tolist()