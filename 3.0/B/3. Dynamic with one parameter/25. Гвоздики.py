num_of_nails = int(input())
nails = list(map(int, input().split()))
nails.sort()
dp = [0] * (num_of_nails + 1)
for i in range(2, num_of_nails + 1):
    if i != 3:
        dp[i] = min(dp[i - 1] + nails[i - 1] - nails[i - 2], dp[i - 2] + nails[i - 1] - nails[i - 2])
    else:
        dp[i] = dp[i - 1] + nails[i - 1] - nails[i - 2]
print(dp[-1])
