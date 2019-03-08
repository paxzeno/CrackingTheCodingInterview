import random
import Queue

from node import Node


class Graph:

    def __init__(self):
        self._nodes = []

    def add_node(self, node):
        self._nodes.append(node)

    def get_nodes(self):
        return self._nodes

    def generate_graph(self, number_nodes):
        self._nodes = [None] * number_nodes

        for i in xrange(0, number_nodes):
            self._nodes[i] = Node(i)

        for node in self._nodes:
            # number of children this node will have from 1 to 4 Max
            number_children = random.randint(1, 4)
            for j in xrange(0, number_children):
                child_node_name = -1
                while child_node_name == -1 or child_node_name == node.get_name():
                    child_node_name = random.randint(0, number_nodes - 1)
                node.add_child(self._nodes[child_node_name])

    def depth_first_search(self, node_name):
        return None

    def breath_first_search(self, root_name, find_node_name):
        node = self._nodes[root_name]
        queue = Queue.Queue()
        queue.put(node)

        checked = set()
        checked.add(node)
        path = {}

        while not queue.empty():
            q_node = queue.get()
            self.print_node(q_node)

            for child_node in q_node.get_children():
                if child_node.get_name() not in checked:
                    path[child_node.get_name()] = q_node.get_name()
                    checked.add(child_node.get_name())
                    if child_node.get_name() == find_node_name:
                        return self.print_path(path, root_name, find_node_name)
                    else:
                        queue.put(child_node)

        return self.print_path(None)

    @staticmethod
    def print_path(path, origin=None, end=None):
        if path is None:
            return 'No path found for the node'

        route = str(end)
        pointer = end
        while pointer != origin:
            route += ' -> ' + str(path[pointer])
            pointer = path[pointer]

        return route

    @staticmethod
    def print_node(node):
        print_children = ', Child Nodes: ['
        for child_node in node.get_children():
            print_children += str(child_node.get_name()) + ';'
        print_children += ']'

        print('Node:' + str(node.get_name()) + print_children)


if __name__ == '__main__':
    graph = Graph()
    graph.generate_graph(7)
    print(graph.breath_first_search(0, 2))
