x, y, year = map(int, input().split())
if x > 12:
    print(1)
elif y > 12:
    print(1)
elif x == y:
    print(1)
else:
    print(0)