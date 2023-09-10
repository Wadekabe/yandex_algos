def binary_search(l, r, check, checkparams):
    # возвращает индекс первого подходящего элемента
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def check(index, sticker):
    # проверяте меньше ли наклейка коллекционера, чем у Диего
    if sticker <= diego_stickers[index]:
        return True


# ввод данных
N = int(input())
diego_stickers = list(set(map(int, input().split())))
K = int(input())
col_stickers = list(map(int, input().split()))

# сортировка наклеек по возрастанию, с запоминанием порядка для коллекционеров
diego_stickers.sort()

# вывод данных
for i in col_stickers:
    index = binary_search(0, len(diego_stickers), check, i)
    print(index)
