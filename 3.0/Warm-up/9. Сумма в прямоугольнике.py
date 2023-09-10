if __name__ == "__main__":
    n, m, k = map(int, input().split())
    prefix_sum = [[0] * (m+1) for i in range(n+1)]
    for i in range(1, n+1):
        line = list(map(int, input().split()))
        for col in range(len(line)):
            prefix_sum[i][col+1] = prefix_sum[i-1][col+1] + prefix_sum[i][col] - prefix_sum[i-1][col] + line[col]

    for j in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        print(prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1])