class Henkilo:
    def __init__(self, nimi: str):
        self.nimi = nimi
        

    def anna_etunimi(self):
        lista = [self.nimi.split(" ")]
        etu = lista[0][0]
        return etu

    def anna_sukunimi(self):
        lista = [self.nimi.split(" ")]
        suku = lista[0][1]
        return suku
        
if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())

    pauli = Henkilo("Pauli Pythonen")
    print(pauli.anna_etunimi())
    print(pauli.anna_sukunimi())
