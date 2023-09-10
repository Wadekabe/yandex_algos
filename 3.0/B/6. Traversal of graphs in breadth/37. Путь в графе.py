def graph_reading_from_file(file="input.txt"):
    with open(file) as file:
        vertices = int(file.readline())
        graph = [[] for i in range(vertices + 1)]
        vert = 0
        for i in range(vertices):
            vert += 1
            edges = list(map(int, file.readline().split()))
            for edge in range(len(edges)):
                if edges[edge] == 1:
                    graph[vert].append(edge+1)
        start, fin = map(int, file.readline().split())
    return vertices, graph, start, fin


def bfs(graph, start, fin):
    visited = [-1 for i in range(len(graph))]
    parent = [-1 for i in range(len(graph))]
    visited[start] = 0
    queue = [start]

    while len(queue) > 0:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                queue.append(neighbor)
                visited[neighbor] = visited[current] + 1
                parent[neighbor] = current

    print(visited[fin])
    if visited[fin] > 0:
        path = ""
        vert = fin
        while vert != start:
            path += str(vert) + " "
            vert = parent[vert]
        path += str(start)
        print(*path.split()[::-1])


if __name__ == "__main__":
    vertices, graph, start, fin = graph_reading_from_file("37.txt")
    bfs(graph, start, fin)