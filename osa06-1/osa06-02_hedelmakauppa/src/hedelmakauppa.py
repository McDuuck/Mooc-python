def lue_hedelmat():
    lista = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(";")
            lista[osat[0]] = float(osat[1])
    return lista
    
    


if __name__ == "__main__":
    lue_hedelmat()