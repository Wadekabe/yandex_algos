# вводы данных
N = int(input())
diego_stickers = list(set(map(int, input().split())))
K = int(input())
stickers = list(map(int, input().split()))

# сортировка наклеек по возрастанию, с запоминанием порядка для коллекционеров
diego_stickers.sort()
col_stickers = []
for i in range(len(stickers)):
    col_stickers.append([stickers[i], i, 0])
col_stickers = sorted(col_stickers, key=lambda x: x[0])

# вычисление количества стикеров
end = len(diego_stickers) - 1
for sticker in range(len(col_stickers) - 1, -1, -1):
    p = col_stickers[sticker][0]
    for diego_sticker in range(end, -1, -1):
        if p > diego_stickers[diego_sticker]:
            end = diego_sticker
            col_stickers[sticker][2] = end + 1
            break

# возвращение исходного порядка и вывод данных
col_stickers = sorted(col_stickers, key=lambda x: x[1])
for i in col_stickers:
    print(i[2])
