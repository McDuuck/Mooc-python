
class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta

    def suurempi(self, verrattava):
        if self.nelioita > verrattava.nelioita:
            return True
        else:
            return False

    def hintaero(self, verrattava):
        eka = self.nelioita * self.neliohinta
        toka = verrattava.nelioita * verrattava.neliohinta
        if eka > toka:
            return eka - toka
        else:
            return toka - eka

    def kalliimpi(self, verrattava):
        if self.neliohinta * self.nelioita > verrattava.neliohinta * verrattava.nelioita:
            return True
        else:
            return False

if __name__ == "__main__":
    eira_yksio = Asunto(1, 16, 5500)
    kallio_kaksio = Asunto(2, 38, 4200)
    jakomaki_kolmio = Asunto(3, 78, 2500)

    print(eira_yksio.kalliimpi(kallio_kaksio))
    print(jakomaki_kolmio.kalliimpi(kallio_kaksio))