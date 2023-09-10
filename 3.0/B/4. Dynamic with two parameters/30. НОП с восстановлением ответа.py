n = int(input())
subseq1 = list(map(int, input().split()))
m = int(input())
subseq2 = list(map(int, input().split()))

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

for line in range(1, n + 1):
    for column in range(1, m + 1):
        if subseq1[line - 1] == subseq2[column - 1]:
            dp[line][column] = dp[line - 1][column - 1] + 1
        else:
            dp[line][column] = max(dp[line][column - 1], dp[line - 1][column])

ans = []
line_now = n
column_now = m
while line_now > 0 and column_now > 0:
    if subseq1[line_now - 1] == subseq2[column_now - 1]:
        ans.append(subseq1[line_now - 1])
        line_now -= 1
        column_now -= 1
    elif dp[line_now][column_now] == dp[line_now - 1][column_now]:
        line_now -= 1
    else:
        column_now -= 1

print(" ".join(str(ans[i]) for i in range(len(ans) - 1, -1, -1)))
