
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepis = input("koepisteet: ")


def koepisteet(pisteet):
    n1 = 0
    alue = [15, 18, 21, 24, 28]
    while n1 < 5 and pisteet >= alue[n1]:
        n1 += 1
    return n1

def lukumaara(lkm):
    return lkm // 4


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

pisteet = {}
with open(koepis) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        arvo = 0
        for p in range(1, len(osat)):
            arvo += int(osat[p])
        pisteet[osat[0]] = arvo



for nro, maara in tehtavat.items():
    yht = pisteet[nro] + lukumaara(maara)
    print(f"{lista[nro]} {koepisteet(yht)}")

