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

candidates = {}
for i in strings:
    key, val = i.split()
    val = int(val)
    if key not in candidates:
        candidates[key] = 0
    candidates[key] += val
for i in sorted(candidates.keys()):
    print(i, candidates[i])
