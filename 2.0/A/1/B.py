from math import sqrt


def dist(x, y, x1, y1):
    return sqrt(abs(y1 - y) ** 2 + abs(x1 - x) ** 2)

"""
def parallelogram(dots):
    a = (dots[0] + dots[4])/2
    b = (dots[1] + dots[5])/2
    if dist(dots[0], dots[1], dots[6], dots[7]) == dist(dots[2], dots[3], dots[4], dots[5]) and \
            dist(dots[0], dots[1], dots[2], dots[3]) == dist(dots[4], dots[5], dots[6], dots[7]) and \
            (dots[2] + dots[6])/2 == a and (dots[3] + dots[7])/2 == b or (dots[2] + dots[4])/2 == a and (dots[3] + dots[5])/2 == b:
        print('YES')
    else:
        print('NO')
"""
def parallelogram(dots):
    all_length = []
    all_length.append(dist(dots[0], dots[1], dots[2], dots[3]))
    all_length.append(dist(dots[0], dots[1], dots[4], dots[5]))
    all_length.append(dist(dots[0], dots[1], dots[6], dots[7]))
    all_length.append(dist(dots[4], dots[5], dots[2], dots[3]))
    all_length.append(dist(dots[4], dots[5], dots[6], dots[7]))
    all_length.append(dist(dots[2], dots[3], dots[6], dots[7]))
    all_length = sorted(all_length)
    print(all_length)
    if all_length[0] == all_length[1] and all_length[2] == all_length[3] and all_length[4] == all_length[5]:
        print('YES')
    else:
        print('NO')

n = int(input())
dots = []
for i in range(n):
    dots.append(list(map(int, input().split())))
for i in dots:
    parallelogram(i)
