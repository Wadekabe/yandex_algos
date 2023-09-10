a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = 0
for i in a:
    if i in b:
        c += 1
print(c)
