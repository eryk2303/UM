import Incremental_learning
import Build
import Data

##function to print tree
# @param element tree
# @param space
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

training_data, test_data = Data.first_training()
# print_tree(Incremental_learning.incremental_learning(new_data, Build.tree), "")
print_tree(Build.build_tree(training_data), "")


