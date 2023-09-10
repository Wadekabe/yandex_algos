def read_data():
    x = list(map(int, input().split()))[1:]
    for i in range(len(x)):
        x[i] = x[i], i
    x.sort()
    return x


S = int(input())
A = read_data()
B = read_data()
C = read_data()
C.sort(key=lambda x: (x[0], -x[1]))
flag = False

for A_val, A_pos in A:
    C_pos = len(C) - 1
    for B_val, B_pos in B:
        while C_pos > 0 and A_val + B_val + C[C_pos][0] > S:
            C_pos -= 1
        if A_val + B_val + C[C_pos][0] == S and (not flag or (A_pos, B_pos, C_pos) < ans):
            ans = A_pos, B_pos, C[C_pos][1]
            flag = True

if flag:
    print(*ans)
else:
    print('-1')