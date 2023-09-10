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
    n = int(input())
    start = 1
    stack = Stack()
    wagons = list(map(int, input().split()))
    for wagon in wagons:
        stack.push(wagon)
        while stack.back() == start:
            stack.pop()
            start += 1
    if stack.size() > 0:
        print("NO")
    else:
        print("YES")
