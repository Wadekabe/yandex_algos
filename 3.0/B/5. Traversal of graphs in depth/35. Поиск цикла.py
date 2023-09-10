def graph_reading_from_file(file="input.txt"):
    with open(file) as file:
        vertices = int(file.readline())
        graph = [[] for i in range(vertices + 1)]
        vert = 0
        for line in file:
            vert += 1
            edges = list(map(int, line.split()))
            for edge in range(len(edges)):
                if edges[edge] == 1:
                    graph[vert].append(edge+1)
    return vertices, graph


def find_cycle(graph):
    def dfs(node, par=-1):
        visited[node] = 1
        parent[node] = par
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                if dfs(neighbor, node):
                    return True
            elif neighbor != par:
                cycle.append(neighbor)
                current = node
                while current != neighbor:
                    cycle.append(current)
                    current = parent[current]
                return True
        return False

    visited = [0 for i in range(len(graph))]
    parent = [-1 for i in range(len(graph))]
    cycle = []

    for node in range(1, len(graph)):
        if visited[node] == 0 and dfs(node):
            break

    if len(cycle) == 0:
        print("NO")
    else:
        print("YES")
        print(len(cycle))
        print(' '.join(map(str, cycle[::-1])))


if __name__ == "__main__":
    vertices, graph = graph_reading_from_file("35.txt")
    find_cycle(graph)
