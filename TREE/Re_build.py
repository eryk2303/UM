import Split
import Build
import  Mesure
import Data

data = Data.secound()
new_tree = None
old_tree = None

def rebuild(tree):
    new_data = None
    if tree[0].false_data is not None:
        new_data = data + tree[0].false_data
    if tree[0].true_data is not None:
        new_data = data + tree[0].true_data
    if tree[0].true_data is not None and tree[0].false_data is not None:
        new_data = data + tree[0].true_data + tree[0].false_data
    if new_data is not None:
        gain, question, true_data, false_data =  Split.make_split(new_data)
        gain_old, question_old, true_old, false_old = Split.check_split(new_data, tree[0].question)
        if gain - gain_old < 0.2:
            if gain == 0:
                return Build.Subtree_Values(None, None, None, gain_old, None, None), Build.Quantity(new_data)

            rebuild(tree[0].right_next)
            rebuild(tree[0].left_next)

            return Build.Subtree_Values(question_old, tree[0].right_next, tree[0].left_next, gain_old, true_old, false_old), Build.Quantity(new_data)
        else:
            if gain == 0:
                return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(new_data)

            right_next = rebuild(tree)
            left_next = rebuild(tree)

            return Build.Subtree_Values(question, right_next, left_next, gain, true_data, false_data), Build.Quantity(new_data)


