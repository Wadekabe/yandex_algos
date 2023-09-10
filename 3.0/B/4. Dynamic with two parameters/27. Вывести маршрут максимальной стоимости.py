n, m = map(int, input().split())
money = []
# заполнение двумерной сетки денег
for i in range(n):
    line = list(map(int, input().split()))
    money.append(line)

# инициализация динамики
dp = [[0 for i in range(m+1)] for j in range(n+1)]

# заполнение динамики: берется максимальное слева или сверху + текущее значение денег
for line in range(len(money)):
    for column in range(len(money[line])):
        dp[line+1][column+1] = max(dp[line][column+1], dp[line+1][column]) + money[line][column]

# возвращение маршрута, проход идёт с последнего элемента, в котором хранится максимальная стоимость, до клетки [1][1]
ans = []
now_line, now_column = n, m
while now_line != 1 or now_column != 1:
    if now_column != 1:
        if dp[now_line][now_column] - dp[now_line][now_column-1] == money[now_line-1][now_column-1]:
            ans.append('R')
            now_column -= 1
        else:
            ans.append('D')
            now_line -= 1
    else:
        ans.append('D')
        now_line -= 1

print(dp[-1][-1])
print(' '.join(str(ans[i]) for i in range(len(ans)-1, -1, -1)))

