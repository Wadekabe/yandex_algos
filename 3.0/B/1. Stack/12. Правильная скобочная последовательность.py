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

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []


if __name__ == "__main__":
    stack = Stack()
    bracket_sequence = input()
    for bracket in bracket_sequence:
        if bracket == "(":
            stack.push(bracket)
        if bracket == "[":
            stack.push(bracket)
        if bracket == "{":
            stack.push(bracket)
        if bracket == ")":
            if stack.back() == "(":
                stack.pop()
            else:
                stack.push(bracket)
                break
            pass
        if bracket == "]":
            if stack.back() == "[":
                stack.pop()
            else:
                stack.push(bracket)
                break
        if bracket == "}":
            if stack.back() == "{":
                stack.pop()
            else:
                stack.push(bracket)
                break
    if stack.size() > 0:
        print("no")
    else:
        print("yes")
