from linkedlist import LinkedList


# this I start with the head node
def delete_node(linked_list, node_name):
    if linked_list.next() is not None:
        p1 = linked_list
        p2 = linked_list.next()

        while p2.name() != node_name and p2.next() is not None:
            p1 = p1.next()
            p2 = p2.next()

        p1.set_next(p2.next())


# this I start with the node to delete
def delete_node(node):
    next_node = node.next()

    # while next_node is not None:
    node.set_next(next_node.next())
    node.set_name(next_node.name())
    node.set_value(next_node.value())


def print_linked_list(llist):
    while llist is not None:
        print('[Node name: ' + str(llist.name()) + ', Value: ' + str(llist.value()) + ']')
        llist = llist.next()


if __name__ == '__main__':
    linked_list = LinkedList.prefill_linked_list(10)
    linked_list.print_linked_list()
    # delete_node(linked_list, 4)
    delete_node(linked_list.get_node(4))
    linked_list.print_linked_list()
