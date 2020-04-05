import Incremental_learning
import Build
import Data


def first_test():
    data_training, data_test = Data.first_training()
    tree = Build.build_tree(data_training)
    test(tree, data_test)


def secound_test():
    data_training_old, data_test_old = Data.first_training()
    data_training, data_test = Data.secound_training()
    test(Incremental_learning.incremental_learning(data_training + data_training_old,
                                                   Build.build_tree(data_training_old))
         , data_test)


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


secound_test()
