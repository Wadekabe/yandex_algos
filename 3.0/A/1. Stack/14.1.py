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
        return -1

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def show_all(self):
        print(self.stack)

    def elements(self):
        return self.stack


if __name__ == "__main__":
    tmp = list(map(int, input().split()))
    n = tmp[0]
    heights = [tmp[i] for i in range(1, len(tmp))]
    stack = Stack()
    max_now = 0
    tmp = []
    for i in heights:
        if stack.size() == 0:
            stack.push(i)
            max_now = i
            continue
        if i == 0:
            while stack.size() > 0:
                stack.pop()
            tmp = []
            continue
        while i < stack.back():
            tmp.append(stack.pop())
        if len(tmp) > 0:
            max_now = max(max_now, min(tmp)*len(tmp))
            tmp = []
        stack.push(i)
    stack.show_all()
    max_now = max(max_now, min(stack.elements()) * stack.size())
    print(max_now)


