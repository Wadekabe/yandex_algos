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

    def all(self):
        return self.stack


if __name__ == "__main__":
    tmp = list(map(int, input().split()))
    n = tmp[0]
    heights = [tmp[i] for i in range(1, len(tmp))]
    stack = Stack()
    tmp = []
    max_now = 0
    for height in heights:
        if stack.size() == 0:
            stack.push(height)
            max_now = height
            continue
        if height == 0:
            while stack.size() > 0:
                stack.pop()
            tmp = []
            continue
        if height >= stack.back():
            stack.push(height)
            tmp.append(height)
            max_now = max(max_now, min(tmp)*len(tmp))
        else:
            stack.push(height)
            max_now = max(max_now, min(stack.all())*stack.size())
    max_now = max(max_now, min(stack.all()) * stack.size())
    print(max_now)




