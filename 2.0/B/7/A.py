n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, "l"))
    segments.append((r, "r"))
segments.sort()
ans = 0
segments_num = 0
for i in range(len(segments)):
    if segments_num > 0:
        ans += segments[i][0] - segments[i - 1][0]
    if segments[i][1] == "l":
        segments_num += 1
    else:
        segments_num -= 1
print(ans)
