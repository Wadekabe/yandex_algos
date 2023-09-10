class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if len(self.stack) >= 1:
            return self.stack.pop()

    def back(self):
        # если стек пустой, то возращает -1, -1, так как в коде в цикле while может произойти обращение к
        # несуществующему элементу
        if len(self.stack) >= 1:
            return self.stack[-1]
        return -1, -1

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def show_all(self):
        print(self.stack)


if __name__ == "__main__":
    n = int(input())
    cost_of_living = list(map(int, input().split()))
    stack = Stack()
    cities = [-1] * n
    for city in range(n):
        city_cost = cost_of_living[city]
        if stack.size() == 0:
            stack.push((city_cost, city))
        else:
            while stack.back()[0] > city_cost:
                cities[stack.pop()[1]] = city
            stack.push((city_cost, city))
    print(" ".join(str(city) for city in cities))


