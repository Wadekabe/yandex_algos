def heapsort(array):
    """
    Пирамидальная сортировка
    """
    def extract(items):
        """
        Преобразовывает массив в кучу для заданного индекса i
        """
        res.append(items[0])
        items[0] = items[-1]
        items.pop(-1)
        heapify(items, 0)

    def heapify(items, i):
        """
        Преобразовывает массив в кучу для заданного индекса i
        ("пропускает" маленькие элементы вниз)
        """
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left + 1 <= len(items):
            if items[left] > items[i]:
                largest = left
        if right + 1 <= len(items):
            if items[right] > items[largest]:
                largest = right
        if largest != i:
            items[i], items[largest] = items[largest], items[i]
            heapify(items, largest)

    res = list()
    index = (len(array) - 2) // 2
    for i in range(index, -1, -1):
        heapify(array, i)
    while len(array) > 0:
        extract(array)
    return res


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    array = heapsort(array)
    print(" ".join(str(num) for num in array[::-1]))


"""
test
9
5 2 8 10 7 4 25 12 3
"""