def read_data():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        x[i] = (x[i], i + 1)
    x.sort()
    return x


n, m = map(int, input().split())
groups = read_data()
audiences = read_data()
aud_num = 0
ans = [0] * (n + 1)
cnt_groups = 0

for student, grp_num in groups:
    while aud_num < len(audiences) and audiences[aud_num][0] < student + 1:
        aud_num += 1
    if aud_num == len(audiences):
        break
    ans[grp_num] = audiences[aud_num][1]
    aud_num += 1
    cnt_groups += 1

print(cnt_groups)
print(*ans[1:])
