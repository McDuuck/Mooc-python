def kertaa_kymmenen(alku: int, loppu: int):
    lista = {}
    n1 = alku
    while n1 < loppu +1:
        lista[n1] = n1 * 10
        n1 += 1
    return lista
if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)
        