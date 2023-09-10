n = int(input())
a = list(map(int, input().split()))
k, maximal, ans = 0, 0, 0
for i in a:
    if i > maximal:
        k = 0
        maximal = i
        k += 1
    elif i == maximal:
        k += 1
for i in a:
    if i != maximal:
        ans += i
print(ans+maximal*(k-1))