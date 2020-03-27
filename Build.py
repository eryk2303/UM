import Split
import sys

sys.setrecursionlimit(10 ** 6)

class Subtree_Values:
    def __init__(self, question, true_branch, false_branch, gain):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
        self.gain = gain


def build_tree(training_data):
    gain, question, true_data, false_data = Split.make_split(training_data)

    if gain == 0:
        return 0


    right_next = build_tree(true_data)

    left_next = build_tree(false_data)

    print("false", false_data)
    print(question)
    return Subtree_Values(question, right_next, left_next, gain)

training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 10, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 30, 'Lemon'],
]



build_tree(training_data)