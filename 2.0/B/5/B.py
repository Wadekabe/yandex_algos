def prefix_sum(array):
    tmp = [0]*(len(array) + 1)
    for i in range(1, len(array)+1):
        tmp[i] = max(array[i-1] + tmp[i-1], 0)
    return tmp[1:]


n = int(input())
array = list(map(int, input().split()))
prefix = prefix_sum(array)
ans = sorted(prefix)[-1]
maximal = max(array)
if ans == 0:
    if ans in array:
        print(ans)
    else:
        print(maximal)
else:
    print(ans)
