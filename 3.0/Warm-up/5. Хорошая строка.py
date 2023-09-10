alphabet = "abcdefghijklmnopqrstuvwxyz"
latin = {}
N = int(input())
for i in range(N):
    num_of_letter = int(input())
    latin[alphabet[i]] = num_of_letter

ans = 0
for i in range(N-1):
    tmp = min(latin[alphabet[i]], latin[alphabet[i+1]])
    latin[alphabet[i]] -= tmp
    ans += tmp

print(ans)




