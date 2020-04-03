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



def first_test():
    quantyty_training = int(0.5*4520*0.8)
    quantyty_training = 100
    first_data_training = data[:quantyty_training]
    quantyty_test = int(0.5 * 4520 * 0.2)
    quantyty_test = 2
    first_data_test = data[quantyty_training:quantyty_test+quantyty_training]
    return first_data_training.values.tolist(), first_data_test.values.tolist()

def secound():
    quantyty_training =130
    first_data_training = data[:100]
    return first_data_training.values.tolist()

