__author__ = '{Eryk Wawrzyn}'

import csv
import pandas as pd
from sklearn.preprocessing import scale



##function to read and optimization data y
# @return data 
def read_data():
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
    return data



##function to read and optimization data agaricus-lepiota
# @return data 
def read_data_second():
    with open('agaricus-lepiota.data') as input_file:
        lines = input_file.readlines()
        newLines = []
        for line in lines:
            newLine = line.strip().split(',')
            newLines.append( newLine )
    data = pd.DataFrame(newLines)

    return data


##function to read and optimization data student-mat
# @return data 
def read_data_third():
    with open('student-mat.csv') as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=';')
        data = pd.DataFrame(list(readCSV))
        tmp = data['Mjob']
        del data['Mjob']
        data['Mjob'] = tmp
    return data

