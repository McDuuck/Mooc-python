def suodata_virheelliset():
    viikko = ''

    for n1 in range(1, 53):
        viikko += str(n1)

    x = ''
    for n1 in range(1, 40):
        x += str(n1)
    
    with open('lottonumerot.csv') as tiedosto:
        oikeet = {}

        for rivi in tiedosto:
            kaikki = {}
            rivi = rivi.replace('\n', '')
            osat = rivi.split(';')
            kaikki[osat[0]] = osat[1]

            for week, numbers in kaikki.items():
                if week[7:] not in viikko:
                    continue
                ero = numbers.split(',')
                tosi = True
                lista = []
                for i in ero:
                    if i not in x or len(ero) != 7:
                        tosi = False
                        break
                for i in ero:
                    if i not in lista:
                        lista.append(i)
                    else:
                        tosi = False
                        break

                if tosi == False:
                    continue
                oikeet[week] = numbers
    with open('korjatut_numerot.csv', 'w') as tiedosto:
        for viikko, lotot in oikeet.items():
            tiedosto.write(f"{viikko};{lotot}\n")

if __name__ == "__main__":
    suodata_virheelliset()