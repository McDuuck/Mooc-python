# TEE RATKAISUSI TÄHÄN:
class Paivays:
    def __init__(self, paiva: int, kuukausi: int, vuosi: int):
        self.paiva = paiva
        self.kuukausi = kuukausi
        self.vuosi = vuosi
        

    def koko(self):
        koko = self.paiva, self.kuukausi, self.vuosi
        return koko
    
    def __str__(self):
        return f'{self.paiva}.{self.kuukausi}.{self.vuosi}'

    def __eq__(self, toinen: "Paivays"):
        if self.vuosi == toinen.vuosi and self.kuukausi == toinen.kuukausi and self.paiva == toinen.paiva:
            return True
        else:
            return False

    def __lt__(self, toinen: "Paivays"):
        if self.vuosi < toinen.vuosi:
            return True
        elif self.vuosi == toinen.vuosi:
            if self.kuukausi < toinen.kuukausi:
                return True
            elif self.kuukausi == toinen.kuukausi:
                if self.paiva < toinen.paiva:
                    return True

        return False

    def __gt__(self, toinen: "Paivays"):
        if self.vuosi > toinen.vuosi:
            return True
        elif self.vuosi == toinen.vuosi:
            if self.kuukausi > toinen.kuukausi:
                return True
            elif self.kuukausi == toinen.kuukausi:
                if self.paiva > toinen.paiva:
                    return True
        
        return False
    # !=
    def __ne__(self, toinen: "Paivays"):
        if self.__eq__(toinen) == False:
            return True
        else:
            return False

    def paivat(self):
        return ((self.vuosi-1)*12*30) + ((self.kuukausi-1)*30) + self.paiva

    def __add__(self, lisaa: int):
        paivat = self.paivat()
        paivat += lisaa
        kuukaus = ((paivat//30)%12)+1
        vuos = (paivat//360)+1
        paiva = paivat % 30
        return Paivays(paiva, kuukaus, vuos)

    def __sub__(self, toinen: "Paivays"):
        nykyiset = self.paivat()
        toiset = toinen.paivat()
        return abs(nykyiset - toiset)

if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)
