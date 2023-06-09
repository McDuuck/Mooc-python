def etsi_elokuvat(rekisteri: list, hakusana: str):
    haku = []
    for elokuva in rekisteri:
        if hakusana in elokuva["nimi"].lower():
            haku.append(elokuva)

    return haku






if __name__ == "__main__":
    rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
    {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
    {"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

    lista = etsi_elokuvat(rekisteri, "python")
    print(lista)