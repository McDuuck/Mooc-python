from datetime import datetime
from string import digits

def onko_validi(hetu: str):
    if len(hetu) != 11:
        return False
    lista = []
    paiva = int(hetu[0:2])
    kuu = int(hetu[2:4])
    vuos = int(hetu[4:6])
    merkki = hetu[6]
    loppu = int(hetu[7:10])
    osa = hetu[10]
    matikka = int(hetu[0:6] + hetu[7:10])
    if osa in digits:
        osa = int(hetu[10])
    if merkki == "+":
        vuos = "18" + hetu[4:6]
    if merkki == "-":
        vuos = "19" + hetu[4:6]
    if merkki == "A":
        vuos = "20" + hetu[4:6]

    for i in hetu[7:10]:
        if i not in digits:
            return False


    if matikka % 31 == 0:
        arvo = 0
    if matikka % 31 == 1:
        arvo = 1
    if matikka % 31 == 2:
        arvo = 2
    if matikka % 31 == 3:
        arvo = 3
    if matikka % 31 == 4:
        arvo = 4
    if matikka % 31 == 5:
        arvo = 5
    if matikka % 31 == 6:
        arvo = 6
    if matikka % 31 == 7:
        arvo = 7
    if matikka % 31 == 8:
        arvo = 8
    if matikka % 31 == 9:
        arvo = 9
    if matikka % 31 == 10:
        arvo = "A"
    if matikka % 31 == 11:
        arvo = "B"
    if matikka % 31 == 12:
        arvo = "C"
    if matikka % 31 == 13:
        arvo = "D"
    if matikka % 31 == 14:
        arvo = "E"
    if matikka % 31 == 15:
        arvo = "F"
    if matikka % 31 == 16:
        arvo = "H"
    if matikka % 31 == 17:
        arvo = "J"
    if matikka % 31 == 18:
        arvo = "K"
    if matikka % 31 == 19:
        arvo = "L"
    if matikka % 31 == 20:
        arvo = "M"
    if matikka % 31 == 21:
        arvo = "N"
    if matikka % 31 == 22:
        arvo = "P"
    if matikka % 31 == 23:
        arvo = "R"
    if matikka % 31 == 24:
        arvo = "S"
    if matikka % 31 == 25:
        arvo = "T"
    if matikka % 31 == 26:
        arvo = "U"
    if matikka % 31 == 27:
        arvo = "V"
    if matikka % 31 == 28:
        arvo = "W"
    if matikka % 31 == 29:
        arvo = "X"
    if matikka % 31 == 30:
        arvo = "Y"
    
    if osa != arvo:
        return False
    try:
        syntyny = datetime(int(vuos), int(kuu), int(paiva))
    except:
        return False


    return True
    



if __name__ == "__main__":
    print(onko_validi("290200-1239"))
