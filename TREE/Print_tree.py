import Re_build
import Build
import Data


def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""

    print(spacing, node[1].quantity)

    if node[0].question != None:
        print(spacing, str(node[0].question))

    if node[0].true_data != None:
        print(spacing, '--> True:')
        print_tree(node[0].right_next,  spacing + "  ")

    if node[0].false_data != None:
        print(spacing, '--> False:')
        print_tree(node[0].left_next, spacing + "  ")


new_data = Data.secound()
if Build.tree[0].false_data is not None:
    new_data = Data.secound() + Build.tree[0].false_data
if Build.tree[0].true_data is not None:
    new_data = Data.secound() + Build.tree[0].true_data
if Build.tree[0].true_data is not None and Build.tree[0].false_data is not None:
    new_data = Data.secound() + Build.tree[0].true_data + Build.tree[0].false_data

print_tree(Re_build.rebuild(new_data, Build.tree), "")
