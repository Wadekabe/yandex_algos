a = list(map(int, input().split()))
shop_index, house_index = [], []
for i in range(len(a)):
    if a[i] == 1:
        house_index.append(i + 1)
    elif a[i] == 2:
        shop_index.append(i + 1)

maximum, local_minimum = 0, 0
for i in house_index:
    local_minimum = 10
    for j in shop_index:
        if abs(j-i) < local_minimum:
            local_minimum = abs(j-i)
    if local_minimum > maximum:
        maximum = local_minimum
print(maximum)
