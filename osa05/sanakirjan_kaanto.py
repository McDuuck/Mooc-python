def kaanna(sanakirja: dict):
    lista = {}
    for y, x in sanakirja.items():
        lista[x] = y
    sanakirja.clear()
    for y, x in lista.items():
        sanakirja[y] = x

    


if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)