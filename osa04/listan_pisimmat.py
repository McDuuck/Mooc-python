# tee ratkaisu tänne
def pisimmat(lista):
    toka = max(len(x) for x in lista)
    lista = [x for x in lista if len(x) == toka]
    return lista

    




if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimmat(lista)
    print(tulos)
    
    