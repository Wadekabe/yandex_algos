if __name__ == "__main__":
    M = int(input())
    N = int(input())
    sections_b = [False] * N
    sections = []
    for i in range(N):
        a, b = map(int, input().split())
        for k in range(len(sections)):
            ac, bc, ic = sections[k]
            if ac <= b and a <= bc:
                sections_b[ic] = False
        sections.append([a, b, i])
        sections_b[i] = True
    print(sections_b.count(True))
