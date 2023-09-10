n, k = map(int, input().split())
B = list(map(int, input().split()))
maximal = max(B[0], B[1])
minimal = min(B[0], B[1])
for i in range(2, len(B)):
    if B[i] > maximal:
        maximal = B[i]
    elif B[i] < minimal:
        minimal = B[i]
print(maximal-minimal)