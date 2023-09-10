row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
numbers = []
for i in row1:
    numbers.append(i)
for i in row2:
    numbers.append(i)
for i in row3:
    numbers.append(i)
num_rep = {0: 0, 1: 0, 2: 0}
for i in numbers:
    num_rep[i] += 1
k = 0
s = 0
t = 0
if numbers[0] == numbers[1] == numbers[2]:
    if numbers[0] != 0:
        k = numbers[0]
        s += 1
if numbers[3] == numbers[4] == numbers[5]:
    if numbers[3] != 0:
        k = numbers[3]
        s += 1
if numbers[6] == numbers[7] == numbers[8]:
    if numbers[6] != 0:
        k = numbers[6]
        s += 1
if numbers[0] == numbers[3] == numbers[6]:
    if numbers[0] != 0:
        k = numbers[0]
        s += 1
if numbers[1] == numbers[4] == numbers[7]:
    if numbers[1] != 0:
        k = numbers[1]
        s += 1
if numbers[2] == numbers[5] == numbers[8]:
    if numbers[2] != 0:
        k = numbers[2]
        s += 1
if numbers[0] == numbers[4] == numbers[8]:
    if numbers[0] != 0:
        k = numbers[0]
        s += 1
if numbers[2] == numbers[4] == numbers[6]:
    if numbers[2] != 0:
        k = numbers[2]
        s += 1
if s == 1:
    if k == 1:
        t = 2
    else:
        t = 1
    if num_rep[t] + 1 == num_rep[k] or num_rep[t] == num_rep[k]:
        print('YES')
    else:
        print('NO')
elif s == 0:
    if num_rep[2] == 1 and num_rep[1] == 0:
        print('NO')
    elif (num_rep[1]+1 == num_rep[2]) or (num_rep[2]+1 == num_rep[1]) or (num_rep[1] == num_rep[2]) or ((num_rep[0] == 9)):
        print('YES')
    else:
        print('NO')
else:
    print('NO')


