def days(day, akbmx):
    a, k, b, m, x = akbmx
    return a*day - (day//k)*a + b*day - (day//m)*b >= x


def lbin(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


a, k, b, m, x = map(int, input().split())
print(lbin(0, x, days, (a, k, b, m, x)))