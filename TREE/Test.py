
__author__ = '{Eryk Wawrzyn}'

import Correctness_of_building
import Print_tree
import Data_matching
import csv

def read_file(name, arrange):
    with open(name, 'a') as test_file:           
        test_file.writelines(str(arrange[:]))
        test_file.writelines('\n')
    test_file.close()


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
                arrange = Data_matching.data_matching_for_basic_tree(i)
                read_file('test_basic.txt', arrange)

            print("drzewo po douczaniu")
            a = 0
            while a <= 0.95:
                a += 0.05
                i = 0
                while i is not 1:
                    i += 0.05
                    print(a, "ze zbioru - zbiór testowy (0.2 całego zbioru)")
                    print(i, ", ", 1 - i, "piersze trenowanie, douczanie")
                    arrange = Data_matching.data_matching_for_tree_incremental_learning(i, 1 - 1)
                    read_file('test_incremental_%f.txt' %(a), arrange)

            
        else:
            continue
test()

