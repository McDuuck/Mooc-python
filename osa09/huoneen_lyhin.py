# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi

class Huone:
    def __init__(self):
        self.lista = []
        self.pituus = []
        self.kaikki = []

    def lisaa(self, henkilo: Henkilo):
        self.lista.append(henkilo.nimi)
        self.pituus.append(henkilo.pituus)
        self.kaikki.append(henkilo)

    def on_tyhja(self):
        if len(self.lista) > 0:
            return False
        else:
            return True
    
    def lyhin(self):
        if self.on_tyhja():
            return None
        
        lyhyin = self.kaikki[0]
        for henkilo in self.kaikki:
            if lyhyin.pituus > henkilo.pituus:
                lyhyin = henkilo
        return lyhyin

    def poista_lyhin(self):
        if self.on_tyhja():
            return None
        lyhin = self.lyhin()
        lyhin_index = self.kaikki.index(lyhin)
        return self.kaikki.pop(lyhin_index)
        

    def tulosta_tiedot(self):
        printti = f'Huoneessa on {len(self.kaikki)} henkilöä, yheispituus {sum(self.pituus)} cm\n'
        for henkilo in self.kaikki:
            printti += f'{henkilo.nimi} ({henkilo.pituus} cm)\n'
        printti = printti.strip()
        print(printti)


if __name__ == "__main__":
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()