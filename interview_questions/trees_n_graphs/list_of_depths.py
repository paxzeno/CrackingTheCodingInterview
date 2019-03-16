from minimal_tree import create_sorted_array
from minimal_tree import minimal_tree
from data_structures.linkedlist.linkedlist import LinkedList


def fill_list(middle_node, visited, linked_lists, depth):
    if middle_node is not None and middle_node not in visited:
        visited.add(middle_node)
        if linked_lists.has_key(depth):
            linked_lists.get(depth).append_to_tail(middle_node.value(), middle_node.value())
        else:
            linked_lists[depth] = LinkedList(middle_node.value(), middle_node.value())

        fill_list(middle_node.left(), visited, linked_lists, depth + 1)
        fill_list(middle_node.right(), visited, linked_lists, depth + 1)

    return linked_lists


if __name__ == '__main__':
    sorted_array = create_sorted_array(10, 0, 100)
    print(sorted_array)
    binary_tree = minimal_tree(sorted_array)
    list_of_depths = fill_list(binary_tree.get_root(), set(), {}, 0)
    for n_depth, linked_list in list_of_depths.items():
        print('Depth: ' + str(n_depth) + ' values: ' + linked_list.print_ll())
