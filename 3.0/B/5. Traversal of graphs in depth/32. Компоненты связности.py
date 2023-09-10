def find_components(graph):
    """
    Функция для поиска компонент связности в графе.
    :param graph: Список смежности, представляющий граф.
    :return: Список компонент связности, каждая из которых представлена списком вершин.
    """
    def dfs(node, visited, component):
        """
        Обход в глубину для поиска компонент связности.
        :param node: Текущая вершина.
        :param visited: Множество посещенных вершин.
        :param component: Текущая компонента связности.
        """
        stack = [node]
        while stack:
            current_node = stack.pop()
            if not visited[current_node]:
                visited[current_node] = True
                component.append(current_node)
                for neighbor in graph[current_node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    visited = [False for i in range(len(graph))]
    components = []
    for node in range(1, len(graph)):
        if not visited[node]:
            component = []
            dfs(node, visited, component)
            components.append(component)
    return components


def print_components(graph):
    """
    Функция для вывода компонент связности графа в заданном формате.
    :param graph: Список смежности, представляющий граф.
    """
    components = find_components(graph)
    print(len(components))
    for component in components:
        print(len(component))
        print(*component)


def graph_reading_from_file(file="input.txt"):
    with open(file) as f:
        vertices, edges = map(int, f.readline().split())
        graph = [[] for i in range(vertices + 1)]
        for edges in f:
            vert1, vert2 = map(int, edges.split())
            if vert1 != vert2:
                graph[vert1].append(vert2)
                graph[vert2].append(vert1)
            else:
                graph[vert1].append(vert2)
    return vertices, edges, graph


if __name__ == "__main__":
    vertices, edges, graph = graph_reading_from_file("2.txt")
    print_components(graph)
