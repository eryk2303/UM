import Split
import Mesure
import Data



class Subtree_Values:
    def __init__(self, question, true_data, false_data, gain):
        self.question = question
        self.true_data = true_data
        self.false_data = false_data
        self.gain = gain

class Quantity:
    def __init__(self, data):
        self.quantity = Mesure.count(data)

def build_tree(training_data):
    gain, question, true_data, false_data = Split.make_split(training_data)

    if gain == 0:
        return Subtree_Values(None, None, None, gain), Quantity(training_data)

    right_next = build_tree(true_data)
    left_next = build_tree(false_data)

    return Subtree_Values(question[1], right_next, left_next, gain), Quantity(training_data)

training_data, test_data = Data.first_test()

tree = build_tree(training_data)
