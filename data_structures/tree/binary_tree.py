class Tree:
    def __init__(self, root_node):
        self._root_node = root_node

    def set_root(self, root_node):
        self._root_node = root_node

    def get_root(self):
        return self._root_node

    def in_order_traversal_root(self):
        self.in_order_traversal(self._root_node)

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left())
            node.visit()
            self.in_order_traversal(node.right())
