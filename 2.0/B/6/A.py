def lbin(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def rbin(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l


def lcheck_num(num, board):
    return array[num] >= board


def rcheck_num(num, board):
    return array[num] <= board


n = int(input())
array = list(map(int, input().split()))
array.sort()
k = int(input())
ans = []

for i in range(k):
    l, r = map(int, input().split())
    r_ans = rbin(0, len(array) - 1, rcheck_num, r)
    l_ans = lbin(0, len(array) - 1, lcheck_num, l)
    if l <= array[l_ans] <= r and l <= array[r_ans] <= r:
        ans.append(r_ans - l_ans + 1)
    else:
        ans.append(0)

print(*ans)
