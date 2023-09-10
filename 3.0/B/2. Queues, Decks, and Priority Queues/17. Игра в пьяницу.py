class Queue:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.insert(0, n)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("error")

    def front(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            print("error")

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []


def drunkard(queue1, queue2):
    elem1, elem2 = queue1.pop(), queue2.pop()
    if elem1 == 0 and elem2 == 9:
        queue1.push(elem1)
        queue1.push(elem2)
    elif elem1 == 9 and elem2 == 0:
        queue2.push(elem1)
        queue2.push(elem2)
    elif elem1 > elem2:
        queue1.push(elem1)
        queue1.push(elem2)
    elif elem2 > elem1:
        queue2.push(elem1)
        queue2.push(elem2)


if __name__ == "__main__":
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    queue1 = Queue()
    queue2 = Queue()
    for i in range(5):
        queue1.push(first[i])
        queue2.push(second[i])
    check = 0
    while check < 10**6:
        check += 1
        drunkard(queue1, queue2)
        if queue1.size() == 0 or queue2.size() == 0:
            break
    if queue1.size() == 0:
        print("second", check)
    elif queue2.size() == 0:
        print("first", check)
    else:
        print("botva")

