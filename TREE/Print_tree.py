import Incremental_learning
import Build
import Data


def print_tree(element, space=""):
    print(space, element[1].quantity)

    if element[0].question is not None:
        print(space, str(element[0].question))

    if element[0].true_data is not None:
        print(space, 'True:')
        print_tree(element[0].right_next, space + "  ")

    if element[0].false_data is not None:
        print(space, 'False:')
        print_tree(element[0].left_next, space + "  ")


new_data = Data.secound_training()
if Build.tree[0].false_data is not None:
    new_data = Data.secound_training() + Build.tree[0].false_data
if Build.tree[0].true_data is not None:
    new_data = Data.secound_training() + Build.tree[0].true_data
if Build.tree[0].true_data is not None and Build.tree[0].false_data is not None:
    new_data = Data.secound_training() + Build.tree[0].true_data + Build.tree[0].false_data

#print_tree(Incremental_learning.incremental_learning(new_data, Build.tree), "")
print_tree(Build.tree, "")
