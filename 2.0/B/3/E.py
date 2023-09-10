m = int(input())
witnesses = []
for i in range(m):
    witnesses.append(input())
n = int(input())
cars = []
for i in range(n):
    cars.append(input())
numbers = []
maximal = 0
d = 0
for i in cars:
    for k in witnesses:
        if set(k).issubset(i):
            d += 1
    if d > maximal:
        maximal = d
        numbers.clear()
        numbers.append(i)
    elif d == maximal:
        numbers.append(i)
    d = 0
for i in numbers:
    print(i)


