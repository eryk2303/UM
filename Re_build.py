import Split
import Build
import  Mesure

new_data = [
    ['Blue', 3, 'Apple'],
    ['Yellow', 3, 'Grape'],
    ['Black', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 1, 'Lemon'],
]
def count_all(quantity_new_element, quantity_previous):
    count_data = {}
    for count in training_elements:
        # ostatni element
        tmp = count[-1]
        if tmp not in count_data:
            count_data[tmp] = 0
        count_data[tmp] += 1
    return count_data


def re_buidld(new_data, tree):
    quantity_new_element = Mesure.count(new_data)
    quantity_previous = tree[1].quantity


re_buidld(new_data, Build.tree)