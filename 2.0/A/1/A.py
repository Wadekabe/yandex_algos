a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0:
    print('INF')
elif c != 0 and -b / a == -d / c:
    print('NO')
else:
    if -b % a == 0 and -b / a != 0:
        print(int(-b / a))
    else:
        print('NO')
