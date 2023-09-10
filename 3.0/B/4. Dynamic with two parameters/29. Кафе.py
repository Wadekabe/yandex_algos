n = int(input())
cost = [0]
for i in range(n):
    cost.append(int(input()))

# инициализация динамики: dp[day][coupon] - ели на протяжении day дней и после дня day имеем coupon купонов
dp = [[0 for i in range(n + 2)] for j in range(n + 1)]
for column in range(1, n + 2):
    dp[0][column] = 310 * n

# вычисление динамики: либо был потрачен купон, либо был оплачен обед, либо получен купон и оплачен обед
for day in range(1, n + 1):
    for coupon in range(n + 1):
        if cost[day] > 100:
            if coupon == 0:
                dp[day][coupon] = min(dp[day - 1][coupon + 1], dp[day - 1][coupon] + cost[day])
            else:
                dp[day][coupon] = min(dp[day - 1][coupon + 1], dp[day - 1][coupon - 1] + cost[day])
        else:
            dp[day][coupon] = min(dp[day - 1][coupon + 1], dp[day - 1][coupon] + cost[day])

# вычисление минимальной суммарной стоимости обедов и кол-ва купонов, которые останутся для достижения заданной суммы
total_cost, tickets_now = 310 * n, 0
for column in range(len(dp[-1])):
    if dp[-1][column] != 0 and dp[-1][column] <= total_cost:
        total_cost = dp[-1][column]
        tickets_now = column

# нахождение дней, в которые были потрачены купоны, по минимальной сумме
ans = []
cost_now, col_now = total_cost, tickets_now
for day in range(n, 0, -1):
    coupon_used = dp[day - 1][col_now + 1]
    money_spent = dp[day - 1][col_now]
    if dp[day][col_now] - money_spent == cost[day]:
        cost_now = money_spent
    elif dp[day][col_now] == coupon_used:
        col_now += 1
        ans.append(day)
    else:
        col_now -= 1
        cost_now = dp[day - 1][col_now - 1]

# вывод ответа с проверкой, что хотя бы один день обед был платный
if max(cost) == 0:
    print(0)
    print(0, 0)
else:
    print(total_cost)
    print(tickets_now, len(ans))
    for i in reversed(ans):
        print(i)
