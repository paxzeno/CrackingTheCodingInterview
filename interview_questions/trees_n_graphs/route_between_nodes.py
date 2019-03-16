from data_structures.graph.graph import Graph


if __name__ == '__main__':
    graph = Graph()
    graph.generate_graph(15, 2)
    print(graph.breath_first_search(2, 10))
