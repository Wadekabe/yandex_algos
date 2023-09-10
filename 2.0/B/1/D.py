schoolers = int(input())
n = list(map(int, input().split()))
k = sorted(n)
print(k[(len(n)//2)])