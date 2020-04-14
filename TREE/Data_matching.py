import Incremental_learning
import Data
import Build

def data_matching_for_basic_tree(quantity):
    print("Drzewo dla danych określających czy ktoś otrzyma pożyczkę")
    data = Data.read_data()
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training = data[len_data_test:int(len_data_test+data_max_len*quantity)].values.tolist()
    tree = Build.build_tree(data_training)
    data_matching(tree, data_test)
    print("Drzewo dla danych określających jakie ktoś ma wykształcenie")
    data = Data.read_data_second()
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training = data[len_data_test:int(len_data_test+data_max_len*quantity)].values.tolist()
    tree = Build.build_tree(data_training)
    data_matching(tree, data_test)


def data_matching_for_basic_tree_data_without_scale(quantity):
    print("Drzewo dla danych określających czy ktoś otrzyma pożyczkę")
    data = Data.read_data_without_scale()
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training = data[len_data_test:int(len_data_test+data_max_len*quantity)].values.tolist()
    tree = Build.build_tree(data_training)
    data_matching(tree, data_test)



def data_matching_for_tree_incremental_learning(quantity_basic_tree, quantity):
    print("Drzewo dla danych określających czy ktoś otrzyma pożyczkę")
    data = Data.read_data()
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training_first = data[len_data_test:int(len_data_test+data_max_len*quantity_basic_tree)].values.tolist()
    data_training_second = data[int(len_data_test+data_max_len*quantity_basic_tree):int(len_data_test+data_max_len*(quantity_basic_tree+quantity))].values.tolist()
    tree = Build.build_tree(data_training_first)
    tree = Incremental_learning.incremental_learning(data_training_first+data_training_second, tree)
    data_matching(tree, data_test)
    print("Drzewo dla danych określających jakie ktoś ma wykształcenie")
    data = Data.read_data_second()
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training_first = data[len_data_test:int(len_data_test+data_max_len*quantity_basic_tree)].values.tolist()
    data_training_second = data[int(len_data_test+data_max_len*quantity_basic_tree):int(len_data_test+data_max_len*(quantity_basic_tree+quantity))].values.tolist()
    tree = Build.build_tree(data_training_first)
    tree = Incremental_learning.incremental_learning(data_training_first+data_training_second, tree)
    data_matching(tree, data_test)


def data_matching_for_tree_incremental_learning_2(quantity_basic_tree, quantity_1, quantity_2):
    print("Drzewo dla danych określających czy ktoś otrzyma pożyczkę")
    data = Data.read_data()
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training_first = data[len_data_test:int(len_data_test+data_max_len*quantity_basic_tree)].values.tolist()
    data_training_second = data[int(len_data_test+data_max_len*quantity_basic_tree):int(len_data_test+data_max_len*(quantity_basic_tree+quantity_1))].values.tolist()
    data_training_third = data[int(len_data_test+data_max_len*(quantity_basic_tree+quantity_1)):int(len_data_test+data_max_len*(quantity_basic_tree+quantity_1+quantity_2))].values.tolist()
    tree = Build.build_tree(data_training_first)
    tree = Incremental_learning.incremental_learning(data_training_first+data_training_second, tree)
    tree = Incremental_learning.incremental_learning(data_training_first+data_training_second+data_training_third, tree)
    data_matching(tree, data_test)
    print("Drzewo dla danych określających jakie ktoś ma wykształcenie")
    data = Data.read_data_second()
    len_data_test = int(0.2*len(data))
    data_test = data[0:len_data_test].values.tolist()
    data_max_len = len(data) - int(0.2*len(data))
    data_training_first = data[len_data_test:int(len_data_test+data_max_len*quantity_basic_tree)].values.tolist()
    data_training_second = data[int(len_data_test+data_max_len*quantity_basic_tree):int(len_data_test+data_max_len*(quantity_basic_tree+quantity_1))].values.tolist()
    data_training_third = data[int(len_data_test+data_max_len*(quantity_basic_tree+quantity_1)):int(len_data_test+data_max_len*(quantity_basic_tree+quantity_1+quantity_2))].values.tolist()
    tree = Build.build_tree(data_training_first)
    tree = Incremental_learning.incremental_learning(data_training_first+data_training_second, tree)
    tree = Incremental_learning.incremental_learning(data_training_first+data_training_second+data_training_third, tree)
    data_matching(tree, data_test)


##function for calculating test data matching
# @param tree
# @param data test
def data_matching(tree, data_test):
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
    print("Dopasowanie: ", arrange)


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

