class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if len(self.stack) >= 1:
            self.stack.pop()

    def back(self):
        if len(self.stack) >= 1:
            return self.stack[-1]

    def change_last(self, n):
        if len(self.stack) >= 1:
            self.stack[-1] = n

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack = []


if __name__ == "__main__":
    goods = {}
    stack = Stack()
    n = int(input())
    for i in range(n):
        command = list(map(str, input().split()))
        if command[0] == "add":
            num, prod = int(command[1]), command[2]
            if prod not in goods:
                goods[prod] = num
            else:
                goods[prod] += num
            stack.push((prod, num))
        elif command[0] == "delete":
            remain = int(command[1])
            while remain > 0:
                prod, num = stack.back()[0], stack.back()[1]
                if remain >= num:
                    goods[prod] -= num
                    remain -= num
                    stack.pop()
                else:
                    goods[prod] -= remain
                    stack.change_last((prod, num - remain))
                    remain = 0
        elif command[0] == "get":
            prod = command[1]
            if prod in goods:
                print(goods[command[1]])
            else:
                print(0)

