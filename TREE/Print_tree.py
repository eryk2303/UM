import Incremental_learning
import Build
import Data

##function to print tree
# @param element tree
# @param space
def print_tree(element, space=""):
    print(space, element[1].quantity)

    if element[0].question is not None:
        print(space, 'zapytanie', str(element[0].question[1]), ' z kolumny', str(element[0].question[0]))

    if element[0].true_data is not None:
        print(space, 'True:')
        print_tree(element[0].right_next, space + "  ")

    if element[0].false_data is not None:
        print(space, 'False:')
        print_tree(element[0].left_next, space + "  ")


