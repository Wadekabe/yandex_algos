class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, item):
        self.items.append(item)

    def push_back(self, item):
        self.items.insert(0, item)

    def pop_front(self):
        if len(self.items) > 0:
            print(self.items.pop())
        else:
            print("error")

    def pop_back(self):
        if len(self.items) > 0:
            print(self.items.pop(0))
        else:
            print("error")

    def front(self):
        if len(self.items) > 0:
            print(self.items[-1])
        else:
            print("error")

    def back(self):
        if len(self.items) > 0:
            print(self.items[0])
        else:
            print("error")

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items = []


if __name__ == "__main__":
    deque = Deque()
    check = True
    while check:
        commands = list(map(str, input().split()))
        command = commands[0]
        if command == "exit":
            check = False
            print("bye")
        if command == "push_front":
            deque.push_front(commands[1])
            print("ok")
        if command == "pop_front":
            deque.pop_front()
        if command == "front":
            deque.front()
        if command == "push_back":
            deque.push_back(commands[1])
            print("ok")
        if command == "pop_back":
            deque.pop_back()
        if command == "back":
            deque.back()
        if command == "size":
            deque.size()
        if command == "clear":
            deque.clear()
            print("ok")
