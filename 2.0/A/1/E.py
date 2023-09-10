from math import sqrt


def square(a, b, c):
    p = (a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))


p = int(input())
a, b, c, minimal, maximal, a1, b1, c1, a2, b2, c2 = 0, 0, 0, 10**9 + 1, 0, 0, 0, 0, 0, 0, 0
for i in range(1, p+1):
    a = i
    j = p-i
    for k in range(1, j+1):
        b = k
        c = p-a-b
        if c < a+b and c != 0:
            s = square(a, b, c)
            if s > maximal:
                maximal = s
                a2, b2, c2 = a, b, c
            elif s< minimal:
                minimal = s
                a1, b1, c1 = a, b, c
if a2 == b2 == c2 == 0:
    print(-1)
elif a1 == b1 == c1 == 0:
    a1, b1, c1 = a2, b2, c2
    print(a2, b2, c2)
    print(a1, b1, c1)
