def uusi_henkilo(nimi: str, ika: int):
    nimet = nimi.split(" ")
    

    if nimi == "":
        raise ValueError
    if len(nimi) > 40:
        raise ValueError
    if ika < 0:
        raise ValueError
    if ika > 150:
        raise ValueError
    if len(nimet) < 2:
        raise ValueError
    return nimi, ika
        
   

if __name__ == '__main__':
    henkilo = uusi_henkilo("pekka python", 13)
    print(henkilo)