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
    min_elem = 0
    ans = 0
    tmp = []
    for i in heights:
        if stack.size() == 0:
            stack.push(i)
            min_elem = i
            ans = i
            tmp.append(i)
            continue
        if i == 0:
            ans = max(ans, min(tmp) * len(tmp))
            while stack.size() > 0:
                stack.pop()
            tmp = []
            min_elem = 0
            continue
        if i < min_elem:
            min_elem = i
            ans = max(ans, min(tmp)*len(tmp))
            tmp = []
            stack.push(i)
            tmp.append(i)
        else:
            stack.push(i)
            tmp.append(i)
    ans = max(ans, min(stack.elements()) * stack.size())
    print(ans)

