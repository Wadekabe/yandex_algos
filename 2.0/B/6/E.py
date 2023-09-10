n, k = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()
left = 0
right = dots[-1] - dots[0]
while left < right:
    l = (right + left) // 2
    cnt = 0
    maxright = dots[0] - 1
    for dot in dots:
        if dot > maxright:
            cnt += 1
            maxright = dot + l
    if cnt <= k:
        right = l
    else:
        left = l + 1
print(left)