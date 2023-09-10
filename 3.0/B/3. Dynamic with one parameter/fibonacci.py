def fib_rec(n):
    if dp[n] == -1:
        dp[n] = fib_rec(n - 1) + fib_rec(n - 2)
    return dp[n]


def fib_cycle(n):
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[i]


n = int(input())
prog_type = input()
if prog_type == "rec":
    dp = [-1] * (n + 1)
    dp[0] = dp[1] = 1
    print(fib_rec(n))
elif prog_type == "cycle":
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    print(fib_cycle(n))
else:
    print("Нет такого формата")
