from math import sqrt


def dist(a, b):
    return sqrt(abs(b[0] - a[0]) ** 2 + abs(b[1] - a[1]) ** 2)


d = int(input())
x, y = map(int, input().split())
dots = [(d, 0), (0, d)]
minimal = dist((0, 0), (x, y))
top = (0, 0)
if x >= 0 and y >= 0 and y + x <= d:
    print(0)
    exit(0)
else:
    for i in dots:
        if dist(i, (x, y)) < minimal:
            minimal = dist(i, (x, y))
            top = i
if top == (0, 0):
    print(1)
elif top == (d, 0):
    print(2)
else:
    print(3)
