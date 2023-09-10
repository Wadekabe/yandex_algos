def read_subway(file="input.txt"):
    with open(file) as file:
        num_of_stat = int(file.readline())
        num_of_lines = int(file.readline())
        stations = [[] for i in range(num_of_stat + 1)]
        lines = [[] for i in range(num_of_lines + 1)]
        for i in range(1, num_of_lines+1):
            line = list(map(int, file.readline().split()))
            line.pop(0)
            for stat in line:
                lines[i].append(stat)
                stations[stat].append(i)
        A, B = map(int, file.readline().split())
    return lines, stations, A, B


def bfs(lines, stations, A, B):
    visited_lines = [-1 for i in range(len(lines))]
    queue = []
    for line in stations[A]:
        visited_lines[line] = 0
        queue.append(line)
    while len(queue) > 0:
        current_line = queue.pop(0)
        if B in lines[current_line]:
            return visited_lines[current_line]
        else:
            for stat in lines[current_line]:
                for line in stations[stat]:
                    if visited_lines[line] == -1:
                        queue.append(line)
                        visited_lines[line] = visited_lines[current_line] + 1
    return -1


if __name__ == "__main__":
    lines, stations, A, B = read_subway("40_1.txt")
    print(bfs(lines, stations, A, B))

