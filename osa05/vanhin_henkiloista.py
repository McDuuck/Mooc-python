def vanhin(henkilot: list):
    lista = []
    vanhin = []
    
    for henkilo in henkilot:
        vuosi = henkilo[1]
        lista.append(vuosi)
    
    lista.sort()
    
    for nimet in henkilot:
        if lista[0] in nimet:
            vanhin.append(nimet[0])
            
    return vanhin[0]      
    

    







if __name__ == "__main__":
    h1 = ("Arto", 1953)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))