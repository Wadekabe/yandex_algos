maximal = 0
repeats = 0
while True:
    s = int(input())
    if s != 0:
        if s > maximal:
            repeats = 0
            maximal = s
            repeats += 1
        elif s == maximal:
            repeats += 1
    else:
        print(repeats)
        exit(0)

