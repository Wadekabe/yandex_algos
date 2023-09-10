n, k = map(int, input().split())
dp = [0] * 31
start = 2
end = k + 2
tmp = 0
for i in range(2, k+2):
    dp[i] = 2**(i-2)
for i in range(k+2, n+1):
    for j in range(start, end):
        tmp += dp[j]
    dp[i] = tmp
    tmp = 0
    start += 1
    end += 1
print(dp[n])


