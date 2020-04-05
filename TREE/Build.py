import Split
import Mesure
import Data


class Subtree_Values:
    def __init__(self, question, right_next, left_next, gain, true_data, false_data):
        self.question = question
        self.right_next = right_next
        self.left_next = left_next
        self.gain = gain
        self.true_data = true_data
        self.false_data = false_data


class Quantity:
    def __init__(self, data):
        self.quantity = Mesure.count(data)


def count_all(training_data):
    count = Mesure.count(training_data)
    quantity = 0
    for all in count:
        quantity += count[all]
    return quantity


def build_tree(training_data):
    gain, question, true_data, false_data = Split.make_split(training_data)
    if gain == 0:
        return Subtree_Values(None, None, None, gain, None, None), Quantity(training_data)

    right_next = build_tree(true_data)
    left_next = build_tree(false_data)

    return Subtree_Values(question, right_next, left_next, gain, true_data, false_data), Quantity(training_data)


