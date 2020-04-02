import Re_build
import Build

def print_tree(node):
    """World's most elegant tree printing function."""

    print(node[1].quantity)

    if node[0].question != None:
        print(str(node[0].question))

    if node[0].true_data != None:
        print('--> True:')
        print_tree(node[0].right_next)

    if node[0].false_data != None:
        print('--> False:')
        print_tree(node[0].left_next)


print_tree(Re_build.rebuild(Build.tree))
