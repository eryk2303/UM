import Split
import Build
import Mesure
import Data


def rebuild(data, tree):
    gain, question, true_data, false_data = Split.make_split(data)
    if tree is not None:
        if tree[0].right_next is not None:
            gain_old, question_old, true_data_old, false_data_old = Split.check_split(data, tree[0].question)

            if len(tree[0].true_data) and len(tree[0].false_data):
                if Mesure.count(data) is Mesure.count(tree[0].true_data + tree[0].false_data):
                    return Build.Subtree_Values(question, tree[0].right_next, tree[0].left_next, gain, true_data,
                                                false_data), Build.Quantity(data)

            if gain - gain_old > 0.1:

                if gain == 0:
                    return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(data)
                able = True
                if len(tree[0].true_data):
                    if Mesure.count(true_data) == Mesure.count(tree[0].true_data):
                        able = False
                        left_next = rebuild(false_data, tree[0].left_next)
                        return Build.Subtree_Values(question, tree[0].right_next, left_next, gain, true_data,
                                                    false_data), Build.Quantity(data)
                elif len(tree[0].false_data):
                    if Mesure.count(false_data) == Mesure.count(tree[0].false_data):
                        able = False
                        right_next = rebuild(true_data, tree[0].right_next)
                        return Build.Subtree_Values(question, right_next, tree[0].left_next, gain, true_data,
                                                    false_data), Build.Quantity(data)

                if able is True:
                    right_next = rebuild(true_data, tree)
                    left_next = rebuild(false_data, tree)
                    return Build.Subtree_Values(question, right_next, left_next, gain, true_data,
                                                false_data), Build.Quantity(data)

            else:
                if gain_old == 0:
                    return Build.Subtree_Values(None, None, None, gain_old, None, None), Build.Quantity(data)
                able = True
                if len(tree[0].true_data):
                    if Mesure.count(true_data) == Mesure.count(tree[0].true_data):
                        able = False
                        left_next = rebuild(false_data, tree[0].left_next)
                        return Build.Subtree_Values(question, tree[0].right_next, left_next, gain, true_data_old,
                                                    false_data), Build.Quantity(data)
                elif len(tree[0].false_data):
                    if Mesure.count(false_data) == Mesure.count(tree[0].false_data):
                        able = False
                        right_next = rebuild(true_data, tree[0].right_next_next)
                        return Build.Subtree_Values(question, right_next, tree[0].left_next, gain, true_data_old,
                                                    false_data), Build.Quantity(data)

                if able is True:
                    right_next = rebuild(true_data, tree[0].right_next)
                    left_next = rebuild(false_data, tree[0].left_next)
                    return Build.Subtree_Values(question, right_next, left_next, gain_old, true_data_old,
                                                false_data_old), Build.Quantity(data)

        else:
            if gain == 0:
                return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(data)

            right_next = rebuild(true_data, None)
            left_next = rebuild(false_data, None)

            return Build.Subtree_Values(question, right_next, left_next, gain, true_data, false_data), Build.Quantity(
                data)

    else:
        if gain == 0:
            return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(data)

        right_next = rebuild(true_data, None)
        left_next = rebuild(false_data, None)

        return Build.Subtree_Values(question, right_next, left_next, gain, true_data, false_data), Build.Quantity(data)


new_data = Data.secound()
if Build.tree[0].false_data is not None:
    new_data = Data.secound() + Build.tree[0].false_data
if Build.tree[0].true_data is not None:
    new_data = Data.secound() + Build.tree[0].true_data
if Build.tree[0].true_data is not None and Build.tree[0].false_data is not None:
    new_data = Data.secound() + Build.tree[0].true_data + Build.tree[0].false_data

rebuild(new_data, Build.tree)
