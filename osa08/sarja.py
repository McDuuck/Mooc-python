class Sarja:
    def __init__(self, nimi: str, kausi: int, genret: str):
        self.nimi = nimi
        self.kausi = kausi
        self.genret = ", ".join(genret)
        self.arvo = []
        
    def arvostele(self, arvosana: int):
        self.arvo.append(arvosana)

    def keskiarvo(self):
        if len(self.arvo) > 0:
            keskiarvo = sum(self.arvo) / len(self.arvo)
            return round(keskiarvo, 1)
        else:
            return -1

    def __str__(self):
        printti = ''
        printti += f'{self.nimi} ({self.kausi} esityskautta)\n'
        genres_str = self.genret
        printti += f'genret: {genres_str}\n'
        if len(self.arvo) > 0:
            printti += f'arvosteluja {len(self.arvo)}, keskiarvo {self.keskiarvo()} pistettä'
        else:
            printti += 'ei arvosteluja'
        return printti
    
def arvosana_vahintaan(arvosana: float, sarjat: list):
    testi = []
    for sarja in sarjat:
        if sarja.keskiarvo() > arvosana:
            testi.append(sarja)
    return testi

def sisaltaa_genren(genre: str, sarjat: list):
        testi = []
        for sarja in sarjat:
            if genre in sarja.genret.split(", "):
                testi.append(sarja)
        return testi

if __name__ == "__main__":

    dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.arvostele(4)
    dexter.arvostele(5)
    dexter.arvostele(5)
    dexter.arvostele(3)
    dexter.arvostele(0)
    print(dexter)