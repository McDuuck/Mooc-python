# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = []

    def lisaa_luku(self, luku:int):
        self.lukuja.append(luku)

    def lukujen_maara(self):
        return len(self.lukuja)

    def summa(self):
        return sum(self.lukuja) if len(self.lukuja) > 0 else 0

    def keskiarvo(self):
        return sum(self.lukuja) / len(self.lukuja) if len(self.lukuja) > 0 else 0
print('Anna lukuja: ')

stats = Lukutilasto()
tasa = Lukutilasto()
odds = Lukutilasto()
while True:
    luku = int(input(''))
    if luku == -1:
        break
    stats.lisaa_luku(luku)
    tasa.lisaa_luku(luku) if luku % 2 == 0 else odds.lisaa_luku(luku)


tilasto = Lukutilasto()
print(f"Summa: {stats.summa()}")
print(f"Keskiarvo: {stats.keskiarvo()}")
print(f'Parillisten summa: {tasa.summa()}')
print(f'Parittomien summa: {odds.summa()}')
