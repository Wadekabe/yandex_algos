num_of_customers = int(input())
customers = [(3700, 3700, 3700), (3700, 3700, 3700), (3700, 3700, 3700)]
for customer in range(num_of_customers):
    a, b, c = map(int, input().split())
    customers.append((a, b, c))
dp = [0] * len(customers)
for i in range(3, len(customers)):
    dp[i] = min(customers[i][0] + dp[i-1], customers[i-1][1] + dp[i-2], customers[i-2][2] + dp[i-3])
print(dp[-1])
