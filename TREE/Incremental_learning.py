import Split
import Build


##function to find the same tree in old tree
# @param tree - old tree
# @param data current data
def find_tree(tree, data):
    if tree is not None:
        if tree[0].true_data and tree[0].false_data is not None:
            difference_data = [item for item in tree[0].true_data + tree[0].false_data if item not in data]
            if len(difference_data) != 0:
                return None
            difference_tree = [item for item in data if item not in tree[0].true_data + tree[0].false_data]
            if len(difference_tree) == 0 and len(difference_data) == 0:
                return tree
            else:
                if tree[0].right_next is not None:
                    return find_tree(tree[0].right_next, data)
                if tree[0].left_next is not None:
                    return find_tree(tree[0].left_next, data)


##function for incremental learning
# @param tree - old tree
# @param data current data
def incremental_learning(data, tree, quantity):
    if tree is not None:
        if tree[0].right_next and tree[0].left_next is not None:
            gain_old, question_old, true_data_old, false_data_old = Split.check_split(data, tree[0].question)

            tmp_tree = find_tree(tree, data)
            if tmp_tree is not None:
                tree = tmp_tree
                return Build.Subtree_Values(question_old, tree[0].right_next, tree[0].left_next, gain_old, true_data_old,
                                            false_data_old), Build.Quantity(data)

            if gain_old > 0.15:
                if gain_old == 0 or Build.count_all(data) <= quantity*(1/500):
                    return Build.Subtree_Values(None, None, None, gain_old, None, None), Build.Quantity(data)
                right_next = incremental_learning(true_data_old, tree[0].right_next, quantity)
                left_next = incremental_learning(false_data_old, tree[0].left_next, quantity)
                return Build.Subtree_Values(question_old, right_next, left_next, gain_old, true_data_old,
                                            false_data_old), Build.Quantity(data)
            else:

                gain, question, true_data, false_data = Split.make_split(data)

                if gain - gain_old > 0.1 or gain_old <= 0:
                    if gain == 0 or Build.count_all(data) <= quantity*(1/500):
                        return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(data)
                    right_next = incremental_learning(true_data, tree, quantity)
                    left_next = incremental_learning(false_data, tree, quantity)
                    return Build.Subtree_Values(question, right_next, left_next, gain, true_data,
                                                    false_data), Build.Quantity(data)

                else:
                    if gain_old == 0 or Build.count_all(data) <= quantity*(1/500):
                        return Build.Subtree_Values(None, None, None, gain_old, None, None), Build.Quantity(data)
                    right_next = incremental_learning(true_data_old, tree[0].right_next, quantity)
                    left_next = incremental_learning(false_data_old, tree[0].left_next, quantity)
                    return Build.Subtree_Values(question_old, right_next, left_next, gain_old, true_data_old,
                                                    false_data_old), Build.Quantity(data)

        else:
            gain, question, true_data, false_data = Split.make_split(data)
            if gain == 0 or Build.count_all(data) <= quantity*(1/500):
                return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(data)
            right_next = incremental_learning(true_data, None, quantity)
            left_next = incremental_learning(false_data, None, quantity)
            return Build.Subtree_Values(question, right_next, left_next, gain, true_data, false_data), Build.Quantity(
                data)

    else:
        gain, question, true_data, false_data = Split.make_split(data)
        if gain == 0 or Build.count_all(data) <= quantity*(1/500):
            return Build.Subtree_Values(None, None, None, gain, None, None), Build.Quantity(data)
        right_next = incremental_learning(true_data, None, quantity)
        left_next = incremental_learning(false_data, None, quantity)
        return Build.Subtree_Values(question, right_next, left_next, gain, true_data, false_data), Build.Quantity(data)
