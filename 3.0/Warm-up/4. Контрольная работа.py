students = int(input())
variants = int(input())
row = int(input())
place = int(input())
place_pety = (row - 1)*2 + place
if place_pety + variants <= students:
    n = place_pety + variants
    rowdown, placedown = (n + n % 2)//2, 1 if n % 2 else 2
    if place_pety - variants >= 1:
        n = place_pety - variants
        rowup, placeup = (n + n % 2) // 2, 1 if n % 2 else 2
        if abs(row-rowdown) <= abs(row-rowup):
            print(rowdown, placedown)
        else:
            print(rowup, placeup)
    else:
        print(rowdown, placedown)
elif place_pety - variants >= 1:
    n = place_pety - variants
    rowup, placeup = (n + n % 2) // 2, 1 if n % 2 else 2
    print(rowup, placeup)
else:
    print(-1)
