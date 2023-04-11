from datetime import datetime, timedelta

tiedosto = input("Tiedosto: ")
aloitus = input("Aloituspäivä: ")
montako = int(input("Montako päivää: "))
alotus = datetime.strptime(aloitus, '%d.%m.%Y')
vika = alotus + timedelta(days=montako)

print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):")

ajat = []
paivat = []

while alotus < vika:
    paiva = alotus.strftime('%d.%m.%Y')
    paivat.append(paiva)

    ruudut = input(f"Ruutuaika {paiva}: ")
    ajat.append(tuple(ruudut.split(' ')))
    alotus = alotus + timedelta(days=1)


print(f'Tiedot tallennettu tiedostoon {tiedosto}')

with open(tiedosto, 'w') as tieto:
    tieto.write(f'Ajanjakso: {paivat[0]}-{paivat[montako-1]}\n')
    total = 0
    for aika in ajat:
        total += int(aika[0]) + int(aika[1]) + int(aika[2])
    tieto.write(f'Yht. minuutteja: {total}\n')
    tieto.write(f'Keskim. minuutteja: {total/len(ajat)}\n')
    for index, day in enumerate(paivat):
        tieto.write(f'{day}: {ajat[index][0]}/{ajat[index][1]}/{ajat[index][2]}\n')

