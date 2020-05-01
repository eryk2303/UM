
__author__ = '{Eryk Wawrzyn}'

import Correctness_of_building
import Print_tree
import Data_matching
import csv
import datetime
import Data

def write_file(name, arrange):
    with open(name, 'a') as test_file:           
        test_file.writelines(str(arrange[:]))
        test_file.writelines('\n')
    test_file.close()

def write_time(name, time):
    with open(name, 'a') as test_file:           
        test_file.writelines(time)
        test_file.writelines('\n')
    test_file.close()

##function for sending tests
# @param quantity - quantity of data used to tarin dree
# @return arrange - basic tree arrange
def data_matching_for_basic_tree(quantity):
    arrange = []
    print("Drzewo dla zbioru bank")
    data = Data.read_data()
    start = datetime.datetime.now()
    arrange.append(Data_matching.for_basic_tree(quantity, data))
    end = datetime.datetime.now()
    write_time('bank_time_basic.txt', str(end - start))
    print("Drzewo dla zbioru agaricus_incremental")
    data = Data.read_data_second()
    start = datetime.datetime.now()
    arrange.append(Data_matching.for_basic_tree(quantity, data))
    end = datetime.datetime.now()
    write_time('grzyby_time_basic.txt', str(end - start))
    print("Drzewo dla zbioru student")
    data = Data.read_data_third()
    start = datetime.datetime.now()
    arrange.append(Data_matching.for_basic_tree(quantity, data))
    end = datetime.datetime.now()
    write_time('student_time_basic.txt', str(end - start))
    return arrange



##function for sending tests
## @param quantity_basic_tree - quantity of data used to tarin basic tree
# @param quantity - quantity of data used to incremental learning 
# @return arrange - arrange for incremental learning
def data_matching_for_tree_incremental_learning(quantity_basic_tree, quantity, quantity_of_all):
    arrange = []
    print("Drzewo dla zbioru bank")
    data = Data.read_data()
    start = datetime.datetime.now()
    arrange.append(Data_matching.for_tree_incremental_learning(quantity_basic_tree, quantity, data))
    end = datetime.datetime.now()
    write_time('bank_time_incremental_%f.txt' %(quantity_of_all), str(end - start))
    print("Drzewo dla zbioru agaricus_incremental")
    data = Data.read_data_second()
    start = datetime.datetime.now()
    arrange.append(Data_matching.for_tree_incremental_learning(quantity_basic_tree, quantity, data))
    end = datetime.datetime.now()
    write_time('grzyby_time_incremental_%f.txt' %(quantity_of_all), str(end - start))
    print("Drzewo dla zbioru student")
    data = Data.read_data_third()
    start = datetime.datetime.now()
    arrange.append(Data_matching.for_tree_incremental_learning(quantity_basic_tree, quantity, data))
    end = datetime.datetime.now()
    write_time('student_time_incremental_%f.txt' %(quantity_of_all), str(end - start))
    return arrange



##test management function
def test():
    x = 1
    while x is not '0':
        print("Wykonaj gotowy test budowy drzewa - 1")
        print("wykonaj gotowy test dopasowania drzewa - 2")
        print("wyjdz - 0")
        x = input()
        if x is '1':
            print("Budowa podstawowego drzewa dla danych od 20 do 40")
            tree = Correctness_of_building.correctness_of_building(20, 20)
            print("--------------------------------------------------")
            print("Uczenie przyrostowe powyższego drzewa dla danych od 60 do 80")
            Correctness_of_building.correctness_of_incremental(60, 20, tree)


        if x is '2':
            print("podstawowe drzewo")
            i = 0
            
            while i <= 0.95:
                i += 0.05
                print(i, "ze zbioru - zbiór testowy (0.2 całego zbioru)")
                arrange = data_matching_for_basic_tree(i)
                write_file('test_basic.txt', arrange)
                
            print("drzewo po douczaniu")
            a = 0.1
            while a <= 0.95:
                a += 0.05
                i = 0
                while i <= 0.95:
                    i += 0.05
                    print(a, "ze zbioru - zbiór testowy (0.2 całego zbioru)")
                    print(i, ", ", 1 - i, "piersze trenowanie, douczanie")
                    arrange = data_matching_for_tree_incremental_learning(a*i, (1 - i)*a, a)
                    write_file('test_incremental_%f.txt' %(a), arrange)
                    
            
        else:
            continue
test()

