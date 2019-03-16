import random
import Queue

from node import Node


class RoadMap:

    def __init__(self, queue):
        self._queue = queue
        self._path = {}
        self._new_paths = set()

    def get_queue(self):
        return self._queue

    def set_path(self, node_name, parent_node_name):
        # think if there may be some bogus behavior,
        # because of several parents could share the same child node
        self._path[node_name] = parent_node_name

    def get_path(self):
        return self._path

    def set_new_paths(self, paths):
        self._new_paths = paths

    def get_new_paths(self):
        return self._new_paths


class Graph:

    def __init__(self):
        self._nodes = []

    def add_node(self, node):
        self._nodes.append(node)

    def get_nodes(self):
        return self._nodes

    def generate_graph(self, number_nodes, max_number_children=4):
        self._nodes = [None] * number_nodes

        for i in xrange(0, number_nodes):
            self._nodes[i] = Node(i)

        for node in self._nodes:
            # number of children this node will have from 1 to 4 Max
            number_children = random.randint(1, max_number_children)
            for j in xrange(0, number_children):
                child_node_name = -1
                while child_node_name == -1 or child_node_name == node.get_name():
                    child_node_name = random.randint(0, number_nodes - 1)
                node.add_child(self._nodes[child_node_name])

    def depth_first_search(self, node_name):
        # to be implemented
        return None

    def breath_first_search(self, root_name, end_name):
        node = self._nodes[root_name]
        queue = Queue.Queue()
        queue.put(node)

        # TODO no need to have checked and path,
        # TODO path can handle both functions
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
                    if child_node.get_name() == end_name:
                        return self.print_path(path, root_name, end_name)
                    else:
                        queue.put(child_node)

        return self.print_path(None)

    def bidirectional_bfs_search(self, root_name, end_name):
        root_node = self._nodes[root_name]
        end_node = self._nodes[end_name]

        root_queue = Queue.Queue()
        root_queue.put(root_node)

        root_road_map = RoadMap(root_queue)

        found = False
        while not root_road_map.get_queue().empty() and not found:
            root_road_map = self.iterated_bfs_search(root_road_map)
            if end_node in root_road_map.get_new_paths():
                found = True

        if found:
            return self.print_path(root_road_map.get_path(), root_name, end_name)
        return self.print_path(None)

    def iterated_bfs_search(self, road_map):
        queue = road_map.get_queue()
        node = queue.get()

        self.print_node(node)

        children = node.get_children()
        road_map.set_new_paths(children)
        path = road_map.get_path()

        for child_node in children:
            if child_node.get_name() not in path:
                road_map.set_path(child_node.get_name(), node.get_name())
                queue.put(child_node)

        return road_map

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
    graph.generate_graph(20, 2)
    print(graph.breath_first_search(0, 2))
    print(graph.bidirectional_bfs_search(0, 2))
