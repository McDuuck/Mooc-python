
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")


lista = {}


with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        nimet = osat[1] + " " + osat[2].strip()
        lista[osat[0]] = nimet

tehtavat = {}
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        n1 = 0
        for i in range(1, len(osat)):
            n1 += int(osat[i])
        
        tehtavat[osat[0]] = n1

for nro, nimi in lista.items():
    print(f"{nimi} {tehtavat[nro]}")

