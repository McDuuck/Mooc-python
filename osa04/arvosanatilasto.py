def pisteet(lista: list):
    lista = []
    koe = []
    harjotus = []
    while True:
        luku = input("Koepisteet ja harjoitusten määrä: ")
        if luku == "":
            break
        lista.append(luku.split(" "))
        koe.append(lista[0][0])
        harjotus.append(lista[0][1])
        if sum(map(int, harjotus)) < 10:
            harjotus.pop
        lista.clear()
    
    summa = sum(map(int, harjotus))
    summa = int(summa // 10)
    print(summa)
    koesumma = sum(map(int, koe))
    koko = int(summa + koesumma)
    keski = float(koko / len(koe))
    print(round(keski,2))
    return keski


def tulostus(keski):
    print("Tilasto:")
    print("Pisteiden keskiarvo: ",keski)
    print(f"Hyväksymisprosentti: ")
    print("Arvosanajakauma:")
    #print(f"5: ")
    #print(f"4: ")
    #print(f"3: ")
    #print(f"2: ")
    #print(f"1: ")
    #print(f"0: ")
    

def main():
    syote = pisteet(True)
    tulostus(syote)

main()
