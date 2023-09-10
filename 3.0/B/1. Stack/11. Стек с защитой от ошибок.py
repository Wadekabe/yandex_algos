class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if len(self.stack) >= 1:
            print(self.stack.pop())
        else:
            print("error")

    def back(self):
        if len(self.stack) >= 1:
            print(self.stack[-1])
        else:
            print("error")

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack = []


if __name__ == "__main__":
    stack = Stack()
    check = True
    while check:
        commands = list(map(str, input().split()))
        command = commands[0]
        if command == "exit":
            check = False
            print("bye")
        if command == "push":
            stack.push(commands[1])
            print("ok")
        if command == "pop":
            stack.pop()
        if command == "back":
            stack.back()
        if command == "size":
            stack.size()
        if command == "clear":
            stack.clear()
            print("ok")
