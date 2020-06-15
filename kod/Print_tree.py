__author__ = '{Eryk Wawrzyn}'

import Incremental_learning
import Build
import Data

##function used to print tree
# @param element tree
# @param space
def print_tree(element, space=""):
    print(space, element[1].quantity)

    if element[0].question is not None:
        print(space, 'test', str(element[0].question[1]), ' z kolumny', str(element[0].question[0]))

    if element[0].true_data is not None:
        print(space, 'True:')
        print_tree(element[0].right_next, space + "  ")

    if element[0].false_data is not None:
        print(space, 'False:')
        print_tree(element[0].left_next, space + "  ")


##function used to build and print tree
# @param start - the data number in the csv file used to train the tree
# @param quantity - quantity of data used to train the tree
# @param data data for incremental learning
def print_basic_tree(start, quantity, data):
    data = data[start:quantity+start]
    data = data.values.tolist()
    tree = Build.build_tree(data)
    print_tree(tree, "")
    return tree



##function used to incremental learning and print tree
# @param start - the data number in the csv file used to train the tree
# @param quantity - quantity of data used to train the tree
# @param tree - old tree
# @param data data for incremental learning
def print_incremental_tree(start, quantity, tree, data):
    data = data[start:quantity+start]
    data = data.values.tolist()
    tree = Incremental_learning.incremental_learning(data + tree[0].true_data + tree[0].false_data, tree)
    print_tree(tree, "")