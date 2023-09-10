# возвращает количество вхождений элемента в значениях словаря
def count(num, dic):
    tmp = 0
    for i in dic.values():
        if i == num:
            tmp += 1
    return tmp

# создание словаря, в котором ключом является номер сообщения, а значением - номер темы, на которую ссылается сообщение;
# также создается вспомогательный словарь вида: {"номер сообщения": "название темы"}
n = int(input())
messages = {}
main_mes = {}
for i in range(1, n+1):
    number_of_mes = int(input())
    if number_of_mes == 0:
        title = input()
        text = input()
        messages[i] = 0
        main_mes[i] = title
    else:
        text = input()
        if messages[number_of_mes] == 0:
            messages[i] = number_of_mes
        else:
            messages[i] = messages[number_of_mes]

# создание и сортировка словаря вида ["количество сообщений по теме", "номер главного сообщения", "заголовок главного сообщения"]
ans = []
for i in main_mes.keys():
    ans.append([count(i, messages), i, main_mes[i]])
ans = sorted(ans, key=lambda x: [-x[0], x[1]])

# вывод ответа
print(ans[0][2])
