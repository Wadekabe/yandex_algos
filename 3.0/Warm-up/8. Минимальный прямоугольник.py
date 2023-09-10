if __name__ == "__main__":
    k = int(input())
    x, y = map(int, input().split())
    x_min, y_min, x_max, y_max = x, y, x, y
    for i in range(k-1):
        x, y = map(int, input().split())
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y
    print(x_min, y_min, x_max, y_max)
