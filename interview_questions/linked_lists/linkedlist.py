import random


class LinkedList:

    def __init__(self, name, value):
        self._name = name
        self._value = value
        self._next_node = None

    def next(self):
        return self._next_node

    def value(self):
        return self._value

    def name(self):
        return self._name

    def set_next(self, next_node):
        self._next_node = next_node

    def set_name(self, node_name):
        self._name = node_name

    def set_value(self, node_value):
        self._value = node_value

    def append_to_tail(self, name, value):
        end = LinkedList(name, value)
        n = self
        while n._next_node is not None:
            n = n._next_node

        n._next_node = end

    def get_node(self, name):
        node = self
        while node is not None and node.name() != name:
            node = node.next()

        if node is None:
            return None

        return node

    @staticmethod
    def prefill_linked_list(nodes):
        ll = LinkedList(0, random.randint(1, 500))

        for i in xrange(1, nodes):
            ll.append_to_tail(i, random.randint(1, 500))
        return ll

    def print_linked_list(self):
        node = self
        linked_list_string = ''
        while node is not None:
            linked_list_string += '[' + str(node.name()) + ',' + str(node.value()) + '] -> '
            node = node.next()
        print(linked_list_string + 'None')
