__author__ = '{Eryk Wawrzyn}'

import Incremental_learning
import Data
import Build
import Print_tree

##function to do test for basic tree
## @param quantity - quantity of data used to tarin dree
def data_matching_for_basic_tree(quantity):
    arrange = []
    print("Drzewo dla danych określających czy ktoś otrzyma pożyczkę")
    data = Data.read_data()
    arrange.append(for_basic_tree(quantity, data))
    print("Drzewo dla danych określających jaki to grzyb")
    data = Data.read_data_second()
    arrange.append(for_basic_tree(quantity, data))
    print("Drzewo dla danych określających gdzie ktoś pracuje")
    data = Data.read_data_third()
    arrange.append(for_basic_tree(quantity, data))
    return arrange


def for_basic_tree(quantity, data):
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training = data[len_data_test:int(len_data_test+data_max_len*quantity)].values.tolist()
    tree = Build.build_tree(data_training)
    arrange = data_matching(tree, data_test)
    return arrange


##function to do test for tree with one incremental learning 
## @param quantity_basic_tree - quantity of data used to tarin basic tree
# @param quantity - quantity of data used to incremental learning 
def data_matching_for_tree_incremental_learning(quantity_basic_tree, quantity):
    arrange = []
    print("Drzewo dla danych określających czy ktoś otrzyma pożyczkę")
    data = Data.read_data()
    arrange.append(for_tree_incremental_learning(quantity_basic_tree, quantity, data))
    print("Drzewo dla danych określających jaki to grzyb")
    data = Data.read_data_second()
    arrange.append(for_tree_incremental_learning(quantity_basic_tree, quantity, data))
    print("Drzewo dla danych określających gdzie ktoś pracuje")
    data = Data.read_data_third()
    arrange.append(for_tree_incremental_learning(quantity_basic_tree, quantity, data))
    return arrange


def for_tree_incremental_learning(quantity_basic_tree, quantity, data):
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training_first = data[len_data_test:int(len_data_test+data_max_len*quantity_basic_tree)].values.tolist()
    data_training_second = data[int(len_data_test+data_max_len*quantity_basic_tree):int(len_data_test+data_max_len*(quantity_basic_tree+quantity))].values.tolist()
    tree = Build.build_tree(data_training_first)
    tree = Incremental_learning.incremental_learning(data_training_first+data_training_second, tree)
    arrange = data_matching(tree, data_test)
    return arrange

##function for calculating test data matching
# @param tree
# @param data test
def data_matching(tree, data_test):
    good = 0
    bad = 0
    for dt in data_test:
        place = find(tree, dt)
        for p in place:
            if p == dt[-1]:
                good += place[p]
            else:
                bad += place[p]
    
    arrange = good / (good + bad)
    print("Dopasowanie: ", arrange)
    return arrange


##find the list for test data
# @param tree
# @param dt element for which we are looking for a place

def find(tree, dt):
    if tree[0].question is not None:
        place = tree[1].quantity
        if isinstance(tree[0].question[1], int) or isinstance(tree[0].question[1], float):
            if tree[0].question[1] <= dt[tree[0].question[0]]:
                return find(tree[0].right_next, dt)
            else:
                return find(tree[0].left_next, dt)
        else:
            if tree[0].question[1] == dt[tree[0].question[0]]:
                return find(tree[0].right_next, dt)
            else:
                return find(tree[0].left_next, dt)
    else:
        return tree[1].quantity
