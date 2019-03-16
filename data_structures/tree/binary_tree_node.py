class TreeNode:

    def __init__(self, value):
        self._right = None
        self._left = None
        self._value = value

    def set_right(self, node):
        self._right = node

    def right(self):
        return self._right

    def set_left(self, node):
        self._left = node

    def left(self):
        return self._left

    def value(self):
        return self._value

    def visit(self):
        print(self.__str__())

    def __str__(self):
        return str(self._value)
