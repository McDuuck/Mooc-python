sana = input("Sana: ")
merkki = input("Merkki: ")
n1 = sana.find(merkki)
n2 = -1

if n1 != -1:
    n2 = sana.find(merkki, n1 + len(merkki))
if n2 == -1:
    print("Osajono ei esiinny merkkijonossa kahdesti.")
else:
    print(f"Osajonon toinen esiintymä on kohdassa {n2}.")
