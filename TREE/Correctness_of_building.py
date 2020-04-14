__author__ = '{Eryk Wawrzyn}'

import Data
import Build
import Print_tree
import Incremental_learning

##function to build and print tree
# @param start - the data number in the csv file used to train the tree
# @param start - quantity of data used to train the tree
def correctness_of_building(start, quantity):
    data = Data.read_data()
    data = data[start:quantity+start]
    data = data.values.tolist()
    tree = Build.build_tree(data)
    Print_tree.print_tree(tree, "")
    return tree


##function to incremental learning and print tree
# @param start - the data number in the csv file used to train the tree
# @param start - quantity of data used to train the tree
# @param tree - old tree
def correctness_of_incremental(start, quantity, tree):
    data = Data.read_data()
    data = data[start:quantity+start]
    data = data.values.tolist()
    tree = Incremental_learning.incremental_learning(data + tree[0].true_data + tree[0].false_data, tree)
    Print_tree.print_tree(tree, "")