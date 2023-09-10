def reading_fleas(file="input.txt"):
    fleas = []
    with open(file) as f:
        n, m, feed_x, feed_y, q = map(int, f.readline().split())
        for i in range(q):
            fleas.append(list(map(int, f.readline().split())))
    return n, m, feed_x, feed_y, fleas


def fleas_gathering(n, m, feed_x, feed_y, fleas):
    def get_neighbors(x, y):
        """
        Функция возвращает всех соседей, которых можно достигнуть из точки [x, y] на поле [n, m].
        """
        neighbors = []
        possible_neighbors = [[x - 2, y + 1], [x - 1, y + 2], [x + 1, y + 2], [x + 2, y + 1],
                              [x + 2, y - 1], [x + 1, y - 2], [x - 1, y - 2], [x - 2, y - 1]]
        for neighbor in range(len(possible_neighbors)):
            x_n, y_n = possible_neighbors[neighbor]
            if x_n < 1 or x_n > n or y_n < 1 or y_n > m:
                pass
            else:
                neighbors.append(possible_neighbors[neighbor])
        return neighbors

    def bfs():
        visited = [[-1] * (m+1) for i in range(n+1)] # задание поля клеток
        visited[feed_x][feed_y] = 0 # клетка блохи (длина пути равна 0)
        queue = [[feed_x, feed_y]]
        while len(queue) > 0:
            cell_x, cell_y = queue.pop(0)
            neighbors = get_neighbors(cell_x, cell_y)
            for neighbor in neighbors:
                n_x, n_y = neighbor
                if visited[n_x][n_y] == -1:
                    queue.append(neighbor)
                    visited[n_x][n_y] = visited[cell_x][cell_y] + 1

        total_path = 0
        for flea in fleas:
            cur_x, cur_y = flea
            if visited[cur_x][cur_y] != -1:
                total_path += visited[cur_x][cur_y]
            else:
                return -1
        return total_path

    return bfs()


if __name__ == "__main__":
    n, m, feed_x, feed_y, fleas = reading_fleas("38.txt")
    print(fleas_gathering(n, m, feed_x, feed_y, fleas))
