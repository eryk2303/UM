__author__ = '{Eryk Wawrzyn}'

import pandas as pd
from sklearn.preprocessing import scale
import Print_tree
import Data_matching
import csv
import datetime
import Data
import _pickle as pickle

##function to read and optimization bank data 
# @return data 
def read_bank():
    data = Data.read_csv_file('bank.csv')
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

bank = read_bank()
agaricus_incremental = Data.read_data_file('agaricus-lepiota.data')
iris = Data.read_data_file('iris.data')


##function to write match
# @param name name of data 
# @param match 
def write_file(name, match):
    with open(name, 'a') as test_file:           
        test_file.writelines(str(match[:]))
        test_file.writelines('\n')
    test_file.close()


##function to write time
# @param name name of data 
# @param time
def write_time(name, time):
    with open(name, 'a') as test_file:           
        test_file.writelines(time)
        test_file.writelines('\n')
    test_file.close()


##function to write confusion matrix
# @param matrix confusion matrix
# @param name name of data 
def write_dict(matrix, name):
    with open(name, 'a') as file:
     file.write(str(matrix))
     file.writelines('\n')


##function for sending tests
# @param quantity  quantity of data used to tarin dree
# @return match  matching basic tree 
def data_matching_for_basic_tree(quantity, name, data):
    print("Drzewo dla zbioru ", name)
    start = datetime.datetime.now()
    match, matrix = Data_matching.for_basic_tree(quantity, data)
    end = datetime.datetime.now()
    if quantity >= 0.95:
        write_dict(matrix, 'confusion_matrix_for_basic_tree_%s.txt' %(name))
    write_time('%s_time_basic.txt' %(name), str(end - start))
    return match


##function for sending tests
## @param quantity_basic_tree quantity of data used to tarin basic tree
# @param quantity quantity of data used to incremental learning 
# @return match matching for incremental learning
def data_matching_for_tree_incremental_learning(quantity_basic_tree, quantity, quantity_of_all, name, data):
    print("Drzewo dla zbioru ", name)
    start = datetime.datetime.now()
    match, matrix = Data_matching.for_tree_incremental_learning(quantity_basic_tree, quantity, data)
    end = datetime.datetime.now()
    if quantity >= 0.95:
        write_dict(matrix, 'confusion_matrix_for_incremental_%s.txt' %(name))
    write_time('%s_time_incremental_%f.txt' %(name, quantity_of_all), str(end - start))
    return match

##function to do all tests
def test():
    x = 1
    while x is not '0':
        print("Wykonaj gotowy test budowy drzewa - 1")
        print("wykonaj gotowy test dopasowania drzewa - 2")
        print("wyjdz - 0")
        x = input()
        if x is '1':
            print("Budowa podstawowego drzewa dla danych od 20 do 40")
            tree = Print_tree.print_basic_tree(20, 20, bank)
            print("--------------------------------------------------")
            print("Uczenie przyrostowe powyższego drzewa dla danych od 60 do 80")
            Print_tree.print_incremental_tree(60, 20, tree, bank)


        if x is '2':
            print("Podstawowe drzewo")
            i = 0
            
            while i <= 0.95:
                i += 0.05
                print(i, "ze zbioru - zbiór testowy (0.2 całego zbioru)")
                match = []
                match.append(data_matching_for_basic_tree(i, 'bank', bank))
                match.append(data_matching_for_basic_tree(i, 'agaricus_incremental', agaricus_incremental))
                match.append(data_matching_for_basic_tree(i, 'iris', iris))
                write_file('test_basic.txt', match)
                
            print("Drzewo po douczaniu")
            a = 0.1
            while a <= 0.95:
                a += 0.05
                i = 0
                while i <= 0.95:
                    i += 0.05
                    print(a, "ze zbioru - zbiór testowy (0.2 całego zbioru)")
                    print(i, ", ", 1 - i, "piersze trenowanie, douczanie")
                    match = []
                    match.append(data_matching_for_tree_incremental_learning(a*i, (1 - i)*a, a, 'bank', bank))
                    match.append(data_matching_for_tree_incremental_learning(a*i, (1 - i)*a, a, 'agaricus_incremental', agaricus_incremental))
                    match.append(data_matching_for_tree_incremental_learning(a*i, (1 - i)*a, a, 'iris', iris))
                    write_file('test_incremental_%f.txt' %(a), match)
           
        else:
            continue

test()