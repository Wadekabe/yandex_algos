def graph_reading_from_file(file="input.txt"):
    with open(file) as f:
        vertices, edges = map(int, f.readline().split())
        graph = [[] for i in range(vertices + 1)]
        for edg in f:
            vert1, vert2 = map(int, edg.split())
            if vert1 != vert2:
                graph[vert1].append(vert2)
                graph[vert2].append(vert1)
            else:
                graph[vert1].append(vert2)
    return vertices, edges, graph


def two_color(graph):
    def dfs(node, color):
        visited[node] = True
        colors[node] = color
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, 3-color)

    visited = [False for i in range(len(graph))]
    colors = [0 for i in range(len(graph))]
    for node in range(1, len(graph)):
        if not visited[node]:
            dfs(node, 1)
        else:
            for neighbor in graph[node]:
                if colors[neighbor] == colors[node]:
                    return False
    return True


if __name__ == "__main__":
    vertices, edges, graph = graph_reading_from_file()
    print("YES") if two_color(graph) else print("NO")



