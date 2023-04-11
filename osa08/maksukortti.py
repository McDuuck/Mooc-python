class Maksukortti:
    def __init__(self, alkusaldo: float):
        self.saldo = alkusaldo

    def syo_edullisesti(self):
        if self.saldo > 2.60:
            self.saldo -= 2.60

    def syo_maukkaasti(self):
        if self.saldo > 4.60:
            self.saldo -= 4.60

    def lataa_rahaa(self, lisaa: float):
        if lisaa < 0:
            raise ValueError("Kortille ei saa ladata negatiivista summaa")
        self.saldo += lisaa


    def __str__(self):
        return f'Kortilla on rahaa {self.saldo:.1f} euroa'

pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)
pekan_kortti.syo_maukkaasti()
matin_kortti.syo_edullisesti()
print(f'Pekka: {pekan_kortti}')
print(f'Matti: {matin_kortti}')
pekan_kortti.lataa_rahaa(20)
matin_kortti.syo_maukkaasti()
print(f'Pekka: {pekan_kortti}')
print(f'Matti: {matin_kortti}')
pekan_kortti.syo_edullisesti()
pekan_kortti.syo_edullisesti()
matin_kortti.lataa_rahaa(50)
print(f'Pekka: {pekan_kortti}')
print(f'Matti: {matin_kortti}')


