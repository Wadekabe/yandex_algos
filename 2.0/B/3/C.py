a = list(map(int, input().split()))
dictionary = {}
ans = []
for i in set(a):
    dictionary[i] = 0
for i in a:
    dictionary[i] += 1
for i in a:
    if dictionary[i] == 1:
        ans.append(i)
print(' '.join(map(str, ans)))