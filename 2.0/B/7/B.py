n = int(input())
shipments = []
for i in range(n):
    arrival, check_time = map(int, input().split())
    shipments.append((arrival, 1))
    shipments.append((arrival + check_time, -1))
shipments.sort()
ans = 0
shipments_num = 0
for i in shipments:
    if i[1] == -1:
        shipments_num -= 1
    else:
        shipments_num += 1
    ans = max(shipments_num, ans)
print(ans)
