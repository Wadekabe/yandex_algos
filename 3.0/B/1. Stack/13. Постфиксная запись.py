class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if len(self.stack) >= 1:
            return self.stack.pop()

    def back(self):
        if len(self.stack) >= 1:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def show_all(self):
        print(self.stack)


if __name__ == "__main__":
    postfix_expression = list(map(str, input().split()))
    stack = Stack()
    for symbol in postfix_expression:
        try:
            symbol = int(symbol)
        except:
            pass
        if symbol == "+":
            last = stack.pop()
            pre_last = stack.pop()
            stack.push(last + pre_last)
        elif symbol == "-":
            last = stack.pop()
            pre_last = stack.pop()
            stack.push(pre_last - last)
        elif symbol == "*":
            last = stack.pop()
            pre_last = stack.pop()
            stack.push(last * pre_last)
        else:
            stack.push(symbol)
    print(stack.back())
