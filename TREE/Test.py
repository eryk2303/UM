import Incremental_learning
import Build
import Data


##function to do first test 
def first_test():
    data_training, data_test = Data.first_training()
    tree = Build.build_tree(data_training)
    test(tree, data_test)
    return tree

##function to do secound test - secount tree
def secound_test():
    data_training_old, data_test_old = Data.first_training()
    data_training, data_test = Data.secound_training()
    tree = Incremental_learning.incremental_learning(data_training + data_training_old,
                                                   first_test())
    test(tree, data_test)
    return tree

def third_test():
    data_training_old, data_test_old = Data.first_training()
    data_training_old2, data_test_old2 = Data.secound_training()
    data_training, data_test = Data.third_training()
    tree = Incremental_learning.incremental_learning(data_training + data_training_old + data_training_old2,
                                                     secound_test())
    test(tree, data_test)

##function for calculating test data matching
# @param tree
# @param data test
def test(tree, data_test):
    good = 0
    bad = 0
    for dt in data_test:
        place = find(tree, dt, None)
        for p in place:
            if p == dt[-1]:
                good += place[p]
            else:
                bad += place[p]

    arrange = good / (good + bad)
    print(arrange)


##find the list for test data
# @param tree
# @param dt element for which we are looking for a place
# @param place leaf for element df
# @return place leaf for element df
def find(tree, dt, place):
    if tree[0].question is not None:
        if isinstance(tree[0].question[1], int) or isinstance(tree[0].question[1], float):
            if tree[0].question[1] <= dt[tree[0].question[0]]:
                place = tree[1].quantity
                if tree[0].right_next is not None:
                    return find(tree[0].right_next, dt, place)
                else:
                    return place
            else:
                place = tree[1].quantity
                if tree[0].left_next is not None:
                    return find(tree[0].left_next, dt, place)
                else:
                    return place
        else:
            if tree[0].question[1] is dt[tree[0].question[0]]:
                place = tree[1].quantity
                if tree[0].right_next is not None:
                    return find(tree[0].right_next, dt, place)
                else:
                    return place
            else:
                place = tree[1].quantity
                if tree[0].left_next is not None:
                    return find(tree[0].left_next, dt, place)
                else:
                    return place
    else:
        return place

third_test()