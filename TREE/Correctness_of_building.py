import Data
import Build
import Print_tree
import Incremental_learning


def correctness_of_building(start, quantity):
    data = Data.read_data()
    data = data[start:quantity+start]
    data = data.values.tolist()
    tree = Build.build_tree(data)
    Print_tree.print_tree(tree, "")
    return tree

def correctness_of_incremental(start, quantity, tree):
    data = Data.read_data()
    data = data[start:quantity+start]
    data = data.values.tolist()
    tree = Incremental_learning.incremental_learning(data + tree[0].true_data + tree[0].false_data, tree)
    Print_tree.print_tree(tree, "")