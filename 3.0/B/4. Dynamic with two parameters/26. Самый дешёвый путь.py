n, m = map(int, input().split())
penalties = []
# заполнение двумерной сетки штрафов
for i in range(n):
    line = list(map(int, input().split()))
    penalties.append(line)

# инициализация динамики: весь 1 ряд и вся я колонка заполняются 2100 ("бесконечность")
dp = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(m+1):
    dp[0][i] = 2100
for i in range(n+1):
    dp[i][0] = 2100

# заполнение динамики: берется минимальное слева или сверху + текущее значение штрафа
for line in range(len(penalties)):
    for column in range(len(penalties[line])):
        if line == 0 and column == 0:
            dp[line+1][column+1] = penalties[line][column]
        else:
            dp[line+1][column+1] = min(dp[line][column+1], dp[line+1][column]) + penalties[line][column]

print(dp[-1][-1])


