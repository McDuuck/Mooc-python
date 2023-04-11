from random import choice
def heita(noppa: str):
    A = 3, 3, 3, 3, 3, 6
    B = 2, 2, 2, 5, 5, 5
    C = 1, 4, 4, 4, 4, 4
    if noppa == "A":
        return choice(A)
    elif noppa == "B":
        return choice(B)
    else:
        return choice(C)
    
def pelaa(noppa1: str, noppa2: str, kertaa: int):
    n1 = 0
    n2 = 0
    tasa = 0

    for numero in range(kertaa):
        eka = heita(noppa1)
        toka = heita(noppa2)
        if eka > toka:
            n1 += 1
        elif eka < toka:
            n2 += 1
        else:
            tasa += 1

    return n1, n2, tasa





if __name__ == "__main__":
    tulos = pelaa("A", "C", 1000)
    print(tulos)
    tulos = pelaa("B", "B", 1000)
    print(tulos)    