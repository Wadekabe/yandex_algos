from math import ceil, floor


def text_to_int(text):
    """
    Возвращает массив int, содержащий часы, минуты и секунды.
    """
    def check(c):
        if c[0] != 0:
            return int(c)
        else:
            return int(c[1])

    h, m, s = text.split(":")
    h = check(h)
    m = check(m)
    s = check(s)
    return [h, m, s]


def int_to_text(time):
    def check(c):
        if c >= 10:
            return str(c)
        else:
            return "0"+str(c)

    h, m, s = time[0], time[1], time[2]
    h, m, s = check(h), check(m), check(s)
    return h+":"+m+":"+s


def calc_sec(time):
    """
    Считает количество секунд, прошедших с начала дня (00:00) до текущего момента времени.
    """
    return 3600*time[0] + 60*time[1] + time[2]


def plus_sec(time, sec):
    """
    Прибавляет количество секунд к текущему моменту времени. Затем возвращает массив значений.
    """
    time = calc_sec(time)
    time += sec
    time %= 86400
    s = time % 60
    time -= s
    m = time % 3600
    time -= m
    h = time // 3600
    return [h, m//60, s]


def custom_round(num):
    """
    Округляет число по правилам математики.
    """
    if num - floor(num) < 0.5:
        return floor(num)
    else:
        return ceil(num)


if __name__ == "__main__":
    A = input()
    B = input()
    C = input()
    A = text_to_int(A)
    B = text_to_int(B)
    C = text_to_int(C)
    midnight = [24, 0, 0]
    if C[0] > A[0]:
        dif = custom_round((calc_sec(C) - calc_sec(A)) / 2)
    elif C[0] == A[0]:
        if C[1] > A[1]:
            dif = custom_round((calc_sec(C) - calc_sec(A)) / 2)
        elif C[1] == A[1]:
            if C[2] > A[2]:
                dif = custom_round((calc_sec(C) - calc_sec(A)) / 2)
            elif C[2] <= A[2]:
                dif = custom_round((abs((calc_sec(midnight) - calc_sec(A))) + calc_sec(C)) / 2)
        elif C[1] < A[1]:
            dif = custom_round((abs((calc_sec(midnight)-calc_sec(A))) + calc_sec(C))/2)
    elif C[0] < A[0]:
        dif = custom_round((abs((calc_sec(midnight)-calc_sec(A))) + calc_sec(C))/2)

    print(int_to_text(plus_sec(B, dif)))

"""
15:01:00
18:09:45
15:01:40

15:01:00
18:09:45
14:00:59

21:00:00
22:00:00
06:00:00

"""