__author__ = '{Eryk Wawrzyn}'

import Incremental_learning
import Data
import Build
import Print_tree


##function to do test for basic tree
# @param quantity - quantity of data used to tarin dree
# @return arrange - basic tree arrange
# @return matrix - confusion matrix
def for_basic_tree(quantity, data):
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training = data[len_data_test:int(len_data_test+data_max_len*quantity)].values.tolist()
    tree = Build.build_tree(data_training)
    arrange = data_matching(tree, data_test)
    matrix = confusion_matrix(data_test, tree)
    return arrange, matrix



##function to do test for tree with one incremental learning 
## @param quantity_basic_tree - quantity of data used to tarin basic tree
# @param quantity - quantity of data used to incremental learning 
# @return arrange - arrange for incremental learning
# @return matrix - confusion matrix
def for_tree_incremental_learning(quantity_basic_tree, quantity, data):
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - len_data_test
    data_training_first = data[len_data_test:int(len_data_test+data_max_len*quantity_basic_tree)+1].values.tolist()
    data_training_second = data[int(len_data_test+data_max_len*quantity_basic_tree):int(len_data_test+data_max_len*(quantity_basic_tree+quantity))].values.tolist()
    tree = Build.build_tree(data_training_first)
    tree = Incremental_learning.incremental_learning(data_training_first+data_training_second, tree)
    arrange = data_matching(tree, data_test)
    matrix = confusion_matrix(data_test, tree)
    return arrange, matrix

##function for creating confusion matrix
# @param tree
# @param data test
# @return matrix - confusion matrix
def confusion_matrix(data_test, tree):
    matrix = {}
    for dt in data_test:
        place = find(tree, dt)
        tmp = dt[-1]
        if tmp not in matrix:
            matrix[tmp] = {}
        max_value = max(place.values())
        max_keys = [k for k, v in place.items() if v == max_value]
        if max_keys[0] not in matrix[tmp]:
            matrix[tmp][max_keys[0]] = 0 
        matrix[tmp][max_keys[0]] += 1 
    return matrix


##function for calculating test data matching
# @param tree
# @param data test
def data_matching(tree, data_test):
    good = 0
    bad = 0
     
    for dt in data_test:
        place = find(tree, dt)
        max_value = max(place.values())
        max_keys = [k for k, v in place.items() if v == max_value]
        if max_keys[0] == dt[-1]:
            good += 1
        else:
            bad += 1
    
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
