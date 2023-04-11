luku = int(input("Anna luku: "))
n1 = 0

while n1 < luku:
    n1 += 1
    n2 = 0
    while n2 < luku:
        n2 += 1
        print(f"{n1} x {n2} = {n1 * n2}")
