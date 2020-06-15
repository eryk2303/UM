__author__ = '{Eryk Wawrzyn}'

import Split
import Mesure


##class used to save elemnets in all knots
class Subtree_Values:
    ##save information about knots
    def __init__(self, question, right_next, left_next, gain, true_data, false_data):
        ##question used to divide data
        self.question = question
        ##next right knots
        self.right_next = right_next
        ##next left knots
        self.left_next = left_next
        ##gain of information obtained
        self.gain = gain
        ##list with true data - that met the query
        self.true_data = true_data
        ##list with false data - which did not match the query
        self.false_data = false_data

##class used to save information about number of elements
class Quantity:
    ##save information about number of elements
    def __init__(self, data):
        ##number of elements
        self.quantity = Mesure.count(data)


##function used to count all elements
# @param training_elements list in which items will be counted
# @return quantity of elements all elements
def count_all(training_data):
    count = Mesure.count(training_data)
    quantity = 0
    for all in count:
        quantity += count[all]
    return quantity


##function used to build tree
# @param training_elements list of training elements
# @return object Subtree_Values for knot
# @return object Quantity for knot
def build_tree(training_data):
    gain, question, true_data, false_data = Split.make_split(training_data)
    ##when it is impossible to divide, return the leaf
    if gain == 0:
        return Subtree_Values(None, None, None, gain, None, None), Quantity(training_data)

    right_next = build_tree(true_data)
    left_next = build_tree(false_data)

    return Subtree_Values(question, right_next, left_next, gain, true_data, false_data), Quantity(training_data)


