n = int(input())
a = list(map(int, input().split()))
flag = True
for i in range(n-1):
    if a[i+1] < a[i]:
        flag = False
if flag:
    print(a[n-1] - a[0])
else:
    print(-1)