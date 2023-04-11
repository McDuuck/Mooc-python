# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: float):
        self.__eurot = eurot
        self.__sentit = sentit

    def __rahat(self):
        return self.__eurot + (self.__sentit/100)

    def __str__(self):
        return f"{self.__eurot}.{self.__sentit:02d} eur"

    def __eq__(self, toiset: "Raha"):
        return self.__rahat() == toiset.__rahat()

    def __lt__(self, toiset: "Raha"):
        return self.__rahat() < toiset.__rahat()

    def __gt__(self, toiset: "Raha"):
        return self.__rahat() > toiset.__rahat()

    def __ne__(self, toiset: "Raha"):
        return self.__rahat() != toiset.__rahat()

    def __add__(self, toiset: "Raha"):
        eurot = self.__eurot + toiset.__eurot
        sentit = self.__sentit + toiset.__sentit
        if sentit >= 100:
            eurot += 1
        sentit = sentit % 100
        uus = Raha(eurot, sentit)
        return uus

    def __sub__(self, toiset: "Raha"):
        if (self.__rahat() < toiset.__rahat()):
            raise ValueError("negatiivinen tulos ei sallittu")
        eurot = self.__eurot - toiset.__eurot
        if self.__sentit >= toiset.__sentit:
            sentit = self.__sentit - toiset.__sentit
        else:
            eurot -= 1
            sentit = self.__sentit + (100-toiset.__sentit)
        uus = Raha(eurot, sentit)
        return uus
        
if __name__ == "__main__":   
    e1 = Raha(4, 5)
    e2 = Raha(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1