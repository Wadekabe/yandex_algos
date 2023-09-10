def reading_cave_map(file="input.txt"):
    with open(file) as f:
        N = int(f.readline())
        cave_map = [[[-1 for i in range(N + 1)] for j in range(N + 1)] for k in range(N + 1)]
        for i in range(1, N + 1):
            tmp = f.readline()
            for j in range(1, N + 1):
                line = list(f.readline())
                for k in range(1, N + 1):
                    if line[k - 1] == ".":
                        cave_map[i][j][k] = 0
                    elif line[k - 1] == "S":
                        cave_map[i][j][k] = 0
                        start = [i, j, k]
    return N, cave_map, start


def cave_path_len(N, cave_map, start):
    def get_neighbors(d, x, y):
        neighbors = []
        possible_neighbors = [[d, x - 1, y], [d, x, y + 1], [d, x + 1, y],
                              [d, x, y - 1], [d-1, x, y], [d+1, x, y]]
        for neighbor in range(len(possible_neighbors)):
            d_n, x_n, y_n = possible_neighbors[neighbor]
            if d_n < 1 or d_n > N or x_n < 1 or x_n > N or y_n < 1 or y_n > N:
                pass
            else:
                neighbors.append(possible_neighbors[neighbor])
        return neighbors

    def bfs():
        queue = [start]
        while len(queue) > 0:
            d_c, x_c, y_c = queue.pop(0)
            neighbors = get_neighbors(d_c, x_c, y_c)
            for neighbor in neighbors:
                d_n, x_n, y_n = neighbor
                if cave_map[d_n][x_n][y_n] == 0:
                    queue.append(neighbor)
                    cave_map[d_n][x_n][y_n] = cave_map[d_c][x_c][y_c] + 1
                    if d_n == 1:
                        return cave_map[d_n][x_n][y_n]
        return 0

    print(bfs())


if __name__ == "__main__":
    N, cave_map, start = reading_cave_map("39.txt")
    cave_path_len(N, cave_map, start)
