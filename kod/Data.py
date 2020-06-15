__author__ = '{Eryk Wawrzyn}'

import csv
import pandas as pd

##function used to read csv file
# @param name name of data file
# @return data readed data
def read_csv_file(name):
    with open(name) as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=';')
        data = pd.DataFrame(list(readCSV))
    return data


##function used to read data file
# @param name name of data file
# @return data readed data
def read_data_file(name):
    with open(name) as input_file:
        lines = input_file.readlines()
        newLines = []
        for line in lines:
            newLine = line.strip().split(',')
            newLines.append( newLine )
    data = pd.DataFrame(newLines)
    return data



