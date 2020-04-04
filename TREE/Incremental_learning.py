import Split
import Build
import Mesure
import Data


def find_tree(tree, data):
    if tree is not None:
        if tree[0].true_data and tree[0].false_data is not None:
            if Mesure.count(data) == Mesure.count(tree[0].true_data + tree[0].false_data):
                return tree
            else:
                if tree[0].right_next is not None:
                    return find_tree(tree[0].right_next, data)
                if tree[0].left_next is not None:
                    return find_tree(tree[0].left_next, data)
                if tree[0].right_next and tree[0].left_next is not None:
                    return 0


def incremental_learning(data, tree):
    gain, question, true_data, false_data = Split.make_split(data)
    if tree is not None:
        if tree[0].right_next and tree[0].left_next is not None:

            tmp_tree = find_tree(tree, data)
            if tmp_tree is not None:
                if tmp_tree is not 0:
                    tree = tmp_tree
                    return Build.Subtree_Values(question, tree[0].right_next, tree[0].left_next, gain, true_data,
                                                false_data), Build.Quantity(data)


            gain_old, question_old, true_data_old, false_data_old = Split.check_split(data, tree[0].question)

            if gain - gain_old > 0.1 or gain_old is 0:
                if gain == 0:
                    return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(data)
                able = True
                if len(tree[0].true_data):
                    if Mesure.count(true_data) == Mesure.count(tree[0].true_data):
                        able = False
                        left_next = incremental_learning(false_data, tree[0].left_next)
                        return Build.Subtree_Values(question, tree[0].right_next, left_next, gain, true_data,
                                                    false_data), Build.Quantity(data)
                elif len(tree[0].false_data):
                    if Mesure.count(false_data) == Mesure.count(tree[0].false_data):
                        able = False
                        right_next = incremental_learning(true_data, tree[0].right_next)
                        return Build.Subtree_Values(question, right_next, tree[0].left_next, gain, true_data,
                                                    false_data), Build.Quantity(data)

                if able is True:
                    right_next = incremental_learning(true_data, tree)
                    left_next = incremental_learning(false_data, tree)

                    return Build.Subtree_Values(question, right_next, left_next, gain, true_data,
                                                false_data), Build.Quantity(data)

            else:
                if gain_old == 0:
                    return Build.Subtree_Values(None, None, None, gain_old, None, None), Build.Quantity(data)
                able = True
                if len(tree[0].true_data):
                    if Mesure.count(true_data) == Mesure.count(tree[0].true_data):
                        able = False
                        left_next = incremental_learning(false_data, tree[0].left_next)
                        return Build.Subtree_Values(question, tree[0].right_next, left_next, gain, true_data_old,
                                                    false_data), Build.Quantity(data)
                elif len(tree[0].false_data):
                    if Mesure.count(false_data) == Mesure.count(tree[0].false_data):
                        able = False
                        right_next = incremental_learning(true_data, tree[0].right_next_next)
                        return Build.Subtree_Values(question, right_next, tree[0].left_next, gain, true_data_old,
                                                    false_data), Build.Quantity(data)

                if able is True:
                    if gain_old == 0:
                        return Build.Subtree_Values(None, None, None, gain_old, None, None), Build.Quantity(data)
                    right_next = incremental_learning(true_data, tree[0].right_next)
                    left_next = incremental_learning(false_data, tree[0].left_next)
                    return Build.Subtree_Values(question_old, right_next, left_next, gain_old, true_data_old,
                                                false_data_old), Build.Quantity(data)

        else:
            if gain == 0:
                return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(data)
            right_next = incremental_learning(true_data, None)
            left_next = incremental_learning(false_data, None)
            return Build.Subtree_Values(question, right_next, left_next, gain, true_data, false_data), Build.Quantity(
                data)

    else:
        if gain == 0:
            return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(data)
        right_next = incremental_learning(true_data, None)
        left_next = incremental_learning(false_data, None)
        return Build.Subtree_Values(question, right_next, left_next, gain, true_data, false_data), Build.Quantity(data)


