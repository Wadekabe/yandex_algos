if __name__ == "__main__":
    n, m, k = map(int, input().split())
    prefix_sum = [[0] * (m+1) for i in range(n+1)]
    prefix = 0
    for i in range(1, n+1):
        prefix_sum[i][0] = prefix
        line = list(map(int, input().split()))
        for col in range(len(line)):
            prefix += line[col]
            prefix_sum[i][col+1] = prefix

    for j in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        ans = 0
        for string in range(x1, x2 + 1):
            ans += prefix_sum[string][y2] - prefix_sum[string][y1 - 1]
        print(ans)

