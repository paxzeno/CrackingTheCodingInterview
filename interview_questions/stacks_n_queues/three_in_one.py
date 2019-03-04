class A:

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    @staticmethod
    def get_type():
        return 'A'


class B(A):

    def __init__(self, value):
        A.__init__(self, value)

    @staticmethod
    def get_type():
        return 'B'


class C(A):

    def __init__(self, value):
        A.__init__(self, value)

    @staticmethod
    def get_type():
        return 'C'


class ThreeStack:

    def __init__(self, size):
        self._list = [None] * size
        self._PA1 = 0
        self._PA2 = 0
        self._PB1 = size / 3
        self._PB2 = size / 3
        self._PC1 = (size / 3) * 2
        self._PC2 = (size / 3) * 2

    def push(self, item):
        # prevent collisions
        if item.get_type() == 'A':
            self._list[self._PA2] = item
            self._PA2 += 1
            # if self._PA2 == self._PB1:
        if item.get_type() == 'B':
            self._list[self._PB2] = item
            self._PB2 += 1
        if item.get_type() == 'C':
            self._list[self._PC2] = item
            self._PC2 += 1

    def pop_a(self):
        a = self._list[self._PA2 - 1]
        self._list[self._PA2 - 1] = None
        self._PA2 -= 1
        return a

    def pop_b(self):
        self._PB2 -= 1
        return self.pop(self._PB2)

    def pop(self, pointer):
        item = self._list[pointer]
        self._list[pointer] = None
        return item


if __name__ == '__main__':
    a1 = A(1)
    b1 = B(2)
    c1 = C(3)
    a2 = A(2)
    b2 = B(4)
    c2 = C(6)
    a3 = A(4)
    b3 = B(8)
    c3 = C(12)
    a4 = A(8)
    b4 = B(16)
    c4 = C(24)
    stack = ThreeStack(10)
    stack.push(a1)
    stack.push(b1)
    stack.push(c1)
    stack.push(a2)
    stack.push(b2)
    stack.push(c2)
    stack.push(a3)
    stack.push(b3)
    stack.push(c3)
    # stack.add(a4)
    # stack.add(b4)
    # stack.add(c4)

    print('A' + str(stack.pop_a().get_value()))
    print('B' + str(stack.pop_b().get_value()))
    print('B' + str(stack.pop_b().get_value()))
    print('coisas')
