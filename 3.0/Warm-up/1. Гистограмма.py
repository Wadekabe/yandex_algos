message = ""
# ввод данных и удаление пробелов и переносов строки
"""
while True:
    text = input()
    if text:
        message += text + "\n"
    else:
        break
"""
with open("Tests/input1.txt") as file:
    for line in file:
        message += line

message = list(message.replace(" ", "").replace("\n", ""))

# создания словаря "символ - [код символа, количество символов в сообщении]; O(len(message))
symbols = {}
largest_element = 0
for symbol in message:
    if symbol not in symbols:
        symbols[symbol] = [ord(symbol), 1]
        largest_element = max(largest_element, symbols[symbol][1])
    else:
        symbols[symbol][1] += 1
        largest_element = max(largest_element, symbols[symbol][1])

# сортировка словаря по кодам элементов
symbols = sorted(symbols.items(), key=lambda x: x[1][0])

# вывод гистограммы
for i in range(largest_element, 0, -1):
    for symbol in symbols:
        if symbol[1][1] >= i:
            print("#", end="")
        else:
            print(" ", end="")
    print("\n", end="")
for i in symbols:
    print(i[0], end="")




