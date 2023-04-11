import string
import random

def luo_hyva_salasana(maara, numerot, spesiaalit):
    salasana = ''

    pienet = string.ascii_lowercase

    num = string.digits

    spesi = "!?=+-()#"

    sana = pienet

    if numerot == True:
        sana += num

    if spesiaalit == True:
        sana += spesi

    sana2 = random.choices(sana, k=maara)

    if sum(c.isalpha() and c.islower() for c in sana2) == 0:
        sana2[random.randint(0, maara-1)] = random.choice(pienet)

    if numerot and sum(c.isdigit() for c in sana2) == 0:
        sana2[random.randint(0, maara-1)] = random.choice(num)
    if spesiaalit and sum(c in spesi for c in sana2) == 0:
        sana2[random.randint(0, maara-1)] = random.choice(spesi)

    return ''.join(sana2)

if __name__ == "__main__":
    salasana = luo_hyva_salasana(8, False, True)
    print(salasana)