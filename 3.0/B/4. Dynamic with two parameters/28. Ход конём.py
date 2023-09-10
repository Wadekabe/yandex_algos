n, m = map(int, input().split())

# инициализация динамики: dp[i][j] - количество способов попасть в эту клетку, начиная с первой
dp = [[0 for i in range(m + 2)] for j in range(n + 2)]
dp[0][1] = 1

# заполнение динамики: лево-2вверх + 2лево-вверх
for line in range(2, n+2):
    for column in range(2, m+2):
        dp[line][column] = dp[line - 1][column - 2] + dp[line - 2][column - 1]

print(dp[-1][-1])
