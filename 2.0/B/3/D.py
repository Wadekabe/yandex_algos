def set_make(string):
    sett = set()
    tmp = [int(s) for s in string.split() if s.isdigit()]
    for i in tmp:
        sett.add(i)
    return sett


# получение входных данных
n = int(input())
variants = set()
for i in range(1, n+1):
    variants.add(i)
strings = []
stop = ""
while stop != 'HELP':
    stop = input()
    strings.append(stop)

yes = 0
no = 0
for i in range(0, len(strings) - 1, 2):
    if strings[i + 1] == 'YES':
        if yes == 0:
            variants = set_make(strings[i])
            yes += 1
        else:
            variants = variants & set_make(strings[i])
    elif strings[i + 1] == 'NO':
        if no == 0:
            variants = variants - set_make(strings[i])
            no += 1
        else:
            variants -= set_make(strings[i])

ans = []
for i in variants:
    ans.append(i)
ans.sort()
for i in ans:
    print(i, end=' ')
