from Graph import Graph


if __name__ == "__main__":
    vertices, edges = map(int, input().split())
    graph = Graph(vertices, edges)
    graph.graph_reading()
    graph.connect_comp_define()
    num_elem, elems = graph.connect_comp(1)
    print(num_elem)
    for elem in elems:
        print(elem, end=" ")
    """
    test
    10 8
    1 2 
    1 3
    1 4
    1 5
    1 6
    5 7
    6 7
    9 10
    """