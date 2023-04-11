def suurin():
    with open("luvut.txt") as tiedosto:
    
    
        lista = []
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            lista.append(rivi)
        lista.sort()
        isoin = int(lista[-1])
        
        return isoin

if __name__ == "__main__":
    suurin()
        
    

    