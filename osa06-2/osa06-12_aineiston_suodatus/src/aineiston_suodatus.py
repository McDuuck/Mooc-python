def suodata_laskut():
    nimet = []
    lasku = []
    laskut = []
    tulot = []
    with open("laskut.csv") as tiedosto, open('oikeat.csv', 'w') as oikeat, open('vaarat.csv', 'w') as vaarat:
        for rivi in tiedosto:
            rivi = rivi.replace('\n', '')
            osat = rivi.split(";")
            nimet.append(osat[0])
            lasku.append(osat[1])
            if '+' in osat[1]:
                numerot = osat[1].split('+')
                summ = int(numerot[0]) + int(numerot[1])
                laskut.append(summ)
            elif '-' in osat[1]:
                numerot = osat[1].split('-')
                ero = int(numerot[0]) - int(numerot[1])
                laskut.append(ero)
            tulot.append(int(osat[2]))

        for n1 in range(len(nimet)):
            if laskut[n1] == tulot[n1]:
                oikeat.write(f"{nimet[n1]};{lasku[n1]};{tulot[n1]}\n")
            else:
                vaarat.write(f"{nimet[n1]};{lasku[n1]};{tulot[n1]}\n")

if __name__ == "__main__":
    suodata_laskut()
