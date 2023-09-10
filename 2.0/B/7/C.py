def segment_check():
    global next_coor, ans

    if not current_segs:
        ans = set()
        return False

    sorted_current = sorted(current_segs, key=lambda x: x[1], reverse=True)
    proper_segment = sorted_current[0]
    ans.add(proper_segment)
    next_coor = proper_segment[1]

    if next_coor >= m:
        return False

    return True


m = int(input())
check = True
events = []
segments = []
i = 0
while check:
    l, r = map(int, input().split())
    if l == r == 0:
        check = False
    else:
        events.append((l, -1, i))
        events.append((r, 1, i))
        segments.append((l, r))
        i += 1
events.append((0, 0, -1))
events.append((m, 0, -1))
events.sort()

current_segs = set()
ans = set()
next_coor = 0

for i in events:
    coor, event_type, index = i
    if event_type == -1:
        current_segs.add(segments[index])
    elif event_type == 1:
        if segments[index] in current_segs:
            current_segs.remove(segments[index])
        if coor == next_coor:
            if not segment_check():
                break
    else:
        if coor == 0:
            if not segment_check():
                break
        else:
            if not current_segs:
                ans = set()
            break

if not ans:
    print("No solution")
else:
    print(len(ans))
    for i in sorted(list(ans)):
        print(i[0], i[1])

"""
45
-20 10
-10 20
15 40
18 42
24 43
25 35
30 50
0 0

"""
