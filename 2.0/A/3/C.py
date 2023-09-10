days, parties = map(int, input().split())
strikes = set(x for x in range(1, days + 1))
ans = set()
try:
    for i in range(6, days+1, 7):
        strikes.remove(i)
        strikes.remove(i+1)
except:
    None
for i in range(parties):
    day, freq = map(int, input().split())
    tmp = set(x for x in range(day, days+1, freq))
    for i in strikes.intersection(tmp):
        ans.add(i)
print(len(ans))


