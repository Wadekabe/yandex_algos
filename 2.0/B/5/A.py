def prefix_sum(array):
    tmp = [0]*(len(array) + 1)
    for i in range(1, len(array)+1):
        tmp[i] = array[i-1] + tmp[i-1]
    return tmp


n, q = map(int, input().split())
array = list(map(int, input().split()))
prefix = prefix_sum(array)
for i in range(q):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l-1])
