def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    lista = {}
    eka = 0
    toka = 0
    kolmas = 0
    for i in henkilo1:
        if i == "tulos1":
            eka += henkilo1[i]
        if i == "tulos2":
            eka += henkilo1[i]
        if i == "tulos3":
            eka += henkilo1[i]
    eka = eka / 3

    for i in henkilo2:
        if i == "tulos1":
            toka += henkilo2[i]
        if i == "tulos2":
            toka += henkilo2[i]
        if i == "tulos3":
            toka += henkilo2[i]
    toka = toka / 3
    
    for i in henkilo3:
        if i == "tulos1":
            kolmas += henkilo3[i]
        if i == "tulos2":
            kolmas += henkilo3[i]
        if i == "tulos3":
            kolmas += henkilo3[i]
    kolmas = kolmas / 3
    tulokset = [eka, toka, kolmas]
    tulokset.sort()
    
    if tulokset[0] == eka:
        return henkilo1
    if tulokset[0] == toka:
        return henkilo2
    if tulokset[0] == kolmas:
        return henkilo3
if __name__ == "__main__":

    henkilo1 = {"nimi": "Keijo", "tulos1": 5, "tulos2": 3, "tulos3": 1}
    henkilo2 = {"nimi": "Reijo", "tulos1": 6, "tulos2": 4, "tulos3": 2}
    henkilo3 = {"nimi": "Anna", "tulos1": 2, "tulos2": 2, "tulos3": 2}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))