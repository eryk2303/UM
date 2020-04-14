import Correctness_of_building
import Print_tree
import Data_matching


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
            print("całość danych")
            Data_matching.data_matching_for_basic_tree(1)
            print("0.75 danych")
            Data_matching.data_matching_for_basic_tree(0.75)
            print("0.5 danych")
            Data_matching.data_matching_for_basic_tree(0.5)
            print("0.25 danych")
            Data_matching.data_matching_for_basic_tree(0.25)
            print("dane bez unormowania")
            Data_matching.data_matching_for_basic_tree_data_without_scale(1)
            print("0.75 danych")
            Data_matching.data_matching_for_basic_tree_data_without_scale(0.75)
            print("0.5 danych")
            Data_matching.data_matching_for_basic_tree_data_without_scale(0.5)
            print("0.25 danych")
            Data_matching.data_matching_for_basic_tree_data_without_scale(0.25)
            print("drzewo po douczaniu")
            print("0.5, 0.5 danych ")
            Data_matching.data_matching_for_tree_incremental_learning(0.5, 0.5)
            print("0.75, 0.25 danych ")
            Data_matching.data_matching_for_tree_incremental_learning(0.75, 0.25)
            print("0.25, 0.75 danych ")
            Data_matching.data_matching_for_tree_incremental_learning(0.25, 0.75)
            print("0.5, 0.25, 0.25 danych ")
            Data_matching.data_matching_for_tree_incremental_learning_2(0.5, 0.25, 0.25)
            print("0.25, 0.25, 0.5 danych ")
            Data_matching.data_matching_for_tree_incremental_learning_2(0.25, 0.25, 0.5)
            print("0.1, 0.85, 0.05 danych ")
            Data_matching.data_matching_for_tree_incremental_learning_2(0.1, 0.85, 0.05)
        else:
            continue
test()
