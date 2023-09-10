# функция, которая возвращает кортеж, состоящий из названия партии и числа голосов
def vote(string):
    board = string.rfind(' ')
    return string[0:board], int(string[board + 1:len(string)])


# создание словаря "партия: число голосов; создание массива, хранящего порядок получения данных"
order = []
consignment = {}
while True:
    try:
        line = input()
    except BaseException:
        break
    if line:
        key, val = vote(line)
        consignment[key] = val
        order.append(key)
    else:
        break

# задание общего количества голосов, суммы голосов, "первого избирательного частного", а также начальное заполнение словаря с ответами
number_of_votes = 0
sum_of_votes = sum(consignment.values())
first_electoral_private = sum_of_votes / 450
_consignment = {}
ans = {}
for i in consignment.keys():
    votes = int(consignment[i] // first_electoral_private)
    ans[i] = votes
    _consignment[i] = consignment[i] / first_electoral_private - votes
    number_of_votes += votes

# задание массива [["название партии", дробная часть от деления, количество голосов]]
consignment_frac = []
for i in _consignment.keys():
    consignment_frac.append([i, _consignment[i], consignment[i]])
consignment_frac = sorted(consignment_frac, key=lambda element: (-element[1], -element[2]))

# дополнительное заполнение словаря с ответами до достижения 450 голосов
while number_of_votes < 450:
    for i in consignment_frac:
        ans[i[0]] += 1
        number_of_votes += 1
        if number_of_votes >= 450:
            break

# вывод результатов
for i in order:
    print(i, ans[i])
