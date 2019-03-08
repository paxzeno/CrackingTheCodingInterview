class Node:

    def __init__(self, name=-1):
        self._name = name
        self._child_nodes = set()

    def add_child(self, node):
        self._child_nodes.add(node)

    def get_children(self):
        return self._child_nodes

    def get_name(self):
        return self._name
