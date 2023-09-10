def proper_index(index):
    # функция, ищущая ближайшее число с наименьшим количеством операций, которые нужно совершить, чтобы его получить
    minimal = index - 1
    min_paths = dp[index - 1]
    if index % 3 == 0:
        if dp[index // 3] < min_paths:
            minimal = index // 3
            min_paths = dp[index // 3]
    if index % 2 == 0:
        if dp[index // 2] < min_paths:
            minimal = index // 2
            min_paths = dp[index // 2]
    return minimal


def sequence(index):
    # функция, возвращающая последовательность для данного числа
    ans = [index]
    while index != 1:
        if index % 3 == 0 and dp[index // 3] == dp[index] - 1:
            index = index // 3
            ans.append(index)
        elif index % 2 == 0 and dp[index // 2] == dp[index] - 1:
            index = index // 2
            ans.append(index)
        else:
            index = index - 1
            ans.append(index)
    return ans


n = int(input())
dp = [0, 0, 1, 1]
# подсчёт минимального количества операций, необходимых для получения заданного числа
# подсчёт ведётся по всем числам от 4 до n (первые три - база, нулевой элемент не используется)
for i in range(4, n + 1):
    tmp = proper_index(i)
    dp.append(dp[tmp] + 1)

# вывод данных
ans = sequence(n)
print(len(ans)-1)
print(" ".join(str(ans[x]) for x in range(len(ans)-1, -1, -1)))



