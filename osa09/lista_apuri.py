class ListaApuri:
    @classmethod
    def suurin_frekvenssi(cls, lista: list):
        suurin = 1
        suurin_testi = lista[0]
        for i in lista:
            if lista.count(i) > suurin:
                suurin = lista.count(i)
                suurin_testi = i
        return suurin_testi

    @classmethod
    def tuplia(cls, lista: list):
        testi = set(lista)
        tuplat = 0
        for i in testi:
            if lista.count(i) >= 2:
                tuplat += 1
        
        return tuplat


if __name__ == "__main__":
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))