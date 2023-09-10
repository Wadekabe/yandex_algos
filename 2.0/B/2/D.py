l, k = map(int, input().split())
n = list(map(int, input().split()))
min_l, min_r = -1, l
for i in range(len(n)):
    if n[i] < l / 2:
        if n[i] > min_l:
            min_l = n[i]
    elif n[i] >= l / 2:
        if n[i] < min_r:
            min_r = n[i]
if l % 2 == 1 and min_l == l // 2:
    print(min_l)
elif min_l == min_r:
    print(min_l)
else:
    print(min_l, min_r)
