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
m = int(input())
queries = list(map(int, input().split()))

for i in queries:
    r_ans = rbin(0, len(array) - 1, rcheck_num, i)
    l_ans = lbin(0, len(array) - 1, lcheck_num, i)
    if array[l_ans] == i:
        print(l_ans+1, r_ans+1)
    else:
        print(0, 0)
