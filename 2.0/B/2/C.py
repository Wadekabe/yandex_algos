def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


s = input()
minimal = 0
if is_palindrome(s):
    True
else:
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            minimal += 1
print(minimal)