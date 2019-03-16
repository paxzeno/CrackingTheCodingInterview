import random
from data_structures.tree.binary_tree import Tree
from data_structures.tree.binary_tree_node import TreeNode


def minimal_tree(sorted_array):
    root = create_tree(sorted_array, 0, len(sorted_array) - 1)
    tree = Tree(root)
    return tree


def create_tree(array, min, max):
    if min > max:
        return None
    middle = (max + min) / 2
    new_node = TreeNode(array[middle])
    left_sub_tree = create_tree(array, min, middle - 1)
    right_sub_tree = create_tree(array, middle + 1, max)
    new_node.set_left(left_sub_tree)
    new_node.set_right(right_sub_tree)
    return new_node


def create_sorted_array(size, min, max):
    array = [None] * size
    for i in xrange(len(array)):
        array[i] = random.randint(min, max)
    array.sort()
    return array


if __name__ == '__main__':
    array = create_sorted_array(10, 0, 1000)
    print(array)
    minimal_tree(array).in_order_traversal_root()
