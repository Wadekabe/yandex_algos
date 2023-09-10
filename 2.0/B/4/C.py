def count(dic, string):
    for i in string.split():
        if i not in dic:
            dic[i] = 0
        dic[i] += 1


strings = []
while True:
    try:
        line = input()
    except BaseException:
        break
    if line:
        strings.append(line)
    else:
        break

words = {}
for i in strings:
    count(words, i)

ans = []
for i in words.keys():
    ans.append((words[i], i))
ans = sorted(ans, key=lambda element: (-element[0], element[1]))

for i in ans:
    print(i[1])
