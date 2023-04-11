def hae_tiedot(tiedosto: str):
    lista = []
    kirja = {}
    with open(tiedosto) as file:
        for rivi in file:
            rivi = rivi.replace("\n", "")
            lista.append(rivi)
            if len(rivi) > 0:
                kirja[lista[0]] = lista[1:]
            else:
                lista = []
        
    return kirja

def hae_nimi(tiedosto: str, sana: str):
    kirja = hae_tiedot(tiedosto)
    nimet = []
    find = []

    for resepti, aineet in kirja.items():
        nimet.append(resepti)

    for nimi in nimet:
        if sana.lower() in nimi.lower():
            find.append(nimi)

    return find

def hae_aika(tiedosto: str, aika: int):
    kirja = hae_tiedot(tiedosto)
    time = []

    for nimi, tiedot in kirja.items():
        if aika >= int(tiedot[0]):
            time.append(f"{nimi}, valmistusaika {tiedot[0]} min")

    return time



def hae_raakaaine(tiedosto: str, aine: str):
    kirja = hae_tiedot(tiedosto)
    lista = []

    for resepti, info in kirja.items():
        if aine in info:
            lista.append(f"{resepti}, valmistusaika {info[0]} min")

    return lista


