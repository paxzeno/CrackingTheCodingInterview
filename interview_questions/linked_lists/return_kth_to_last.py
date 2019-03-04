from linkedlist import LinkedList


class KthNode:

    def __init__(self):
        self._value = 0
        self._nodes = 0

    def value(self, value):
        self._value = value

    def nodes(self, nodes):
        self._nodes = nodes

    def get_value(self):
        return self._value

    def get_nodes(self):
        return self._nodes


def get_last_node(linked_list, input, kthnode):
    if linked_list is not None:
        value = get_last_node(linked_list.next(), input, kthnode) + 1
        if value == input:
            kthnode.value(linked_list.value())
            return value
        return value
    return 0


def find_kth_recursively(linked_list, input):
    kthnode = KthNode()
    if linked_list.next() is not None:
        number_nodes = get_last_node(linked_list.next(), input, kthnode) + 1
        kthnode.nodes(number_nodes)
    return kthnode


def find_kth_iteratively(linked_list, input):
    if linked_list.next is None:
        return KthNode()

    p1 = linked_list
    p2 = linked_list

    for i in xrange(0, input):
        p1 = p1.next()
        if p1.next() is None:
            return KthNode()
        i += 1

    while p1 is not None:
        p1 = p1.next()
        p2 = p2.next()

    kth = KthNode()
    kth.value(p2.value())
    kth.nodes(0)

    return kth


if __name__ == '__main__':
    input = 3
    linked_list = LinkedList.prefill_linked_list(10)
    kth_rec = find_kth_recursively(linked_list, input)
    kth = find_kth_iteratively(linked_list, input)
    print('The [' + str(kth_rec._nodes - input) + '/' + str(kth_rec.get_nodes()) + '] TH ELEMENT has the VALUE: ' + str(
        kth_rec.get_value()))
    print('The [' + str(kth._nodes - input) + '/' + str(kth.get_nodes()) + '] TH ELEMENT has the VALUE: ' + str(
        kth.get_value()))
