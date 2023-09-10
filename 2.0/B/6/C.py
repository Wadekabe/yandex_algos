def fbinsearch(l, r, eps, check, checkparams):
    while r - l > eps:
        m = (l + r) / 2
        if check(r, m, checkparams):
            r = m
        else:
            l = m
    return l


def cub_root(x, params):
    a, b, c, d = params
    return a * x ** 3 + b * x ** 2 + c * x + d


def check(r, x, params):
    return cub_root(x, params) * cub_root(r, params) > 0


abcd = tuple(map(int, input().split()))
eps = 0.00001
ans = fbinsearch(-1000000, 1000000, eps, check, abcd)
print(ans)
