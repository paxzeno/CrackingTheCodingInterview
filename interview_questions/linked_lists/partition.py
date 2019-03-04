from linkedlist import LinkedList


class PartialList:

    def __init__(self, linked_list=None, last_element=None):
        self._linked_list = linked_list
        self._last_element = last_element

    def get_linked_list(self):
        return self._linked_list

    def get_last_element(self):
        return self._last_element

    def set_linked_list(self, linked_list):
        self._linked_list = linked_list

    def set_last_element(self, last_element):
        self._last_element = last_element


def reorder_list(linked_list, x):
    less_linked_list = PartialList()
    # less_linked_list = None
    equal_more_linked_list = None

    # last_from_less = None
    last_from_more = None

    while linked_list is not None:
        if linked_list.value() < x:
            less_linked_list = add_to_tail(less_linked_list, linked_list)
        else:
            if equal_more_linked_list is None:
                equal_more_linked_list = LinkedList(linked_list.name(), linked_list.value())
                last_from_more = equal_more_linked_list
            else:
                new_node = LinkedList(linked_list.name(), linked_list.value())
                last_from_more.set_next(new_node)
                last_from_more = new_node
        linked_list = linked_list.next()
    less_linked_list.get_last_element().set_next(equal_more_linked_list)
    return less_linked_list.get_linked_list()


def add_to_tail(partial_linked_list, new_element):
    if partial_linked_list.get_linked_list() is None:
        linked_list = LinkedList(new_element.name(), new_element.value())
        return PartialList(linked_list, linked_list)
    else:
        new_node = LinkedList(new_element.name(), new_element.value())
        partial_linked_list.get_last_element().set_next(new_node)
        partial_linked_list.set_last_element(new_node)
    return partial_linked_list


if __name__ == '__main__':
    x = 250
    pre_ordered_list = LinkedList.prefill_linked_list(10)
    pre_ordered_list.print_linked_list()
    partitioned_list = reorder_list(pre_ordered_list, x)
    partitioned_list.print_linked_list()
    # A better solution is to use only one list and push to
    # head or tail, depending if it is less or more
