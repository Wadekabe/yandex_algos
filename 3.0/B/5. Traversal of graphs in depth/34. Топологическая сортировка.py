import sys


def graph_reading_from_file(file="input.txt"):
    with open(file) as f:
        vertices, edges = map(int, f.readline().split())
        graph = [[] for i in range(vertices + 1)]
        for edg in f:
            vert1, vert2 = map(int, edg.split())
            graph[vert1].append(vert2)
    return vertices, edges, graph


def topological(graph):
    def dfs(node):
        visited[node] = 1
        for neighbor in graph[node]:
            if visited[neighbor] == 1:
                nonlocal flag
                flag = 1
            if visited[neighbor] == 0:
                dfs(neighbor)
        visited[node] = 2
        array.append(node)

    flag = 0
    visited = [0 for i in range(len(graph))]
    array = []
    for node in range(1, len(graph)):
        if visited[node] == 0:
            dfs(node)
    return [-1] if flag else array[::-1]


if __name__ == "__main__":
    sys.setrecursionlimit(10000000)
    vertices, edges, graph = graph_reading_from_file("34.txt")
    print(*topological(graph))
