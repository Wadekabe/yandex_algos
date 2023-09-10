s = input()
if len(s) % 2 == 0 and s.count('(') == s.count(')') and s[0] != ')' and s[-1] != '(':
    print('YES')
else:
    print('NO')