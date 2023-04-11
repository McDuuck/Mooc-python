class Tavara:
    def __init__(self, nimi: str, paino: int):
        self.__nimi = nimi
        self.__paino = paino

    def nimi(self):
        return self.__nimi

    def paino(self):
        return self.__paino

    def __str__(self):
        return f'{self.__nimi} ({self.__paino} kg)'

class Matkalaukku:
    def __init__(self, maksimipaino: float):
        self.__laukku = []
        self.__maksimipaino = maksimipaino
        
        
    @property
    def laukku(self):
        return self.__laukku

    def paino(self):
        return sum(item.paino() for item in self.__laukku)

             

    def lisaa_tavara(self, tavara: Tavara):
        current_weight = sum(item.paino() for item in self.__laukku)
        if current_weight + tavara.paino() <= self.__maksimipaino:
            self.__laukku.append(tavara)
          
    def tulosta_tavarat(self):
        for i in self.__laukku:
            print(f'{i}')
        

    def raskain_tavara(self):
        heaviest = self.__laukku[0]
        for item in self.__laukku:
            if item.paino() > heaviest.paino():
                heaviest = item
        return heaviest


    def __str__(self):
        
        if len(self.__laukku) == 1:
            total_weight = sum(tavara.paino() for tavara in self.__laukku)

            return f'{len(self.__laukku)} tavara ({self.paino()} kg)'
        else:
            return f'{len(self.__laukku)} tavaraa ({self.paino()} kg)'



class Lastiruuma:
    def __init__(self, maksimipaino: int):
        self.__maksimipaino = maksimipaino
        self.__matkalaukut = []
        self.__paino = 0

    def lisaa_matkalaukku(self, matkalaukku: Matkalaukku):
        current_weight = sum(laukku.paino() for laukku in self.__matkalaukut)
        if current_weight + matkalaukku.paino() <= self.__maksimipaino:
            self.__matkalaukut.append(matkalaukku)
            self.__maksimipaino -= matkalaukku.paino()

    def tulosta_tavarat(self):
        for matkalaukku in self.__matkalaukut:
            for tavara in matkalaukku.laukku:
                print(tavara)



    def __str__(self):
        if len(self.__matkalaukut) == 1:
            return f'{len(self.__matkalaukut)} matkalaukku, tilaa {self.__maksimipaino} kg'
        else:
            return f'{len(self.__matkalaukut)} matkalaukkua, tilaa {self.__maksimipaino} kg'


if __name__ == "__main__":

    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()