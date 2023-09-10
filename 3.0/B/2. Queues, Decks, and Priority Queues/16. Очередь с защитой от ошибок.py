class Queue:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.insert(0, n)

    def pop(self):
        if len(self.items) > 0:
            print(self.items.pop())
        else:
            print("error")

    def front(self):
        if len(self.items) > 0:
            print(self.items[-1])
        else:
            print("error")

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items = []


if __name__ == "__main__":
    queue = Queue()
    check = True
    while check:
        commands = list(map(str, input().split()))
        command = commands[0]
        if command == "exit":
            check = False
            print("bye")
        if command == "push":
            queue.push(commands[1])
            print("ok")
        if command == "pop":
            queue.pop()
        if command == "front":
            queue.front()
        if command == "size":
            queue.size()
        if command == "clear":
            queue.clear()
            print("ok")
