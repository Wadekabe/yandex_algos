n = int(input())
box = {}
for i in range(n):
    key, val = map(int, input().split())
    if key not in box:
        box[key] = 0
    box[key] += val
for i in sorted(box.keys()):
    print(i, box[i])

