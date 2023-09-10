class Heap():
    def __init__(self):
        self.items = []

    def insert_reg(self, i):
        parent = (i-1)//2
        if parent < 0 or self.items[i] <= self.items[parent]:
            pass
        else:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            self.insert_reg(parent)

    def insert(self, num):
        self.items.append(num)
        self.insert_reg(len(self.items)-1)

    def extract_reg(self, i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        if left + 1 <= len(self.items):
            if self.items[left] > self.items[i]:
                largest = left
        if right + 1 <= len(self.items):
            if self.items[right] > self.items[largest]:
                largest = right
        if largest != i:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            self.extract_reg(largest)

    def extract(self):
        print(self.items[0])
        self.items[0] = self.items[-1]
        self.items.pop(-1)
        self.extract_reg(0)

    def show_heap(self):
        print(self.items)


if __name__  == "__main__":
    heap = Heap()
    n = int(input())
    for i in range(n):
        command = list(map(int, input().split()))
        if command[0] == 0:
            heap.insert(command[1])
        else:
            heap.extract()





