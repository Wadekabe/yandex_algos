n = int(input())
eventsByID = {}
for i in range(n):
    data = input().split()
    day, hour, minute, id = map(int, data[:4])
    event = data[4]
    if event == 'A':
        status = 0
    elif event == 'S' or event == 'C':
        status = 1
    hour = 24*day + hour
    minute = 60*hour + minute
    if id not in eventsByID:
        eventsByID[id] = 0
    if status == 0 and event != 'B':
        eventsByID[id] -= minute
    elif status == 1 and event != 'B':
        eventsByID[id] += minute
for i in sorted(eventsByID):
    print(eventsByID[i], end=' ')

"""
TEST
8
50 7 25 3632 A
14 23 52 212372 S
15 0 5 3632 C
14 21 30 212372 A
50 7 26 3632 C
14 21 30 3632 A
14 21 40 212372 B
14 23 52 3632 B
"""