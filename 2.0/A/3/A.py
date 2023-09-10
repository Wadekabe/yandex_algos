n = int(input())
variants = set(range(1, n+1))
ans = []
while True:
    string = input()
    if string == "HELP":
        break
    else:
        nums = set(map(int, string.split()))
        mat_cnt = len(variants.intersection(nums))
        if mat_cnt <= len(variants)/2:
            ans.append('NO')
            variants = variants - nums
        else:
            ans.append('YES')
            variants = variants.intersection(nums)
for i in ans:
    print(i)
print(*sorted(variants))