# tee ratkaisu tänne
def lyhin(lista):
    lista = min(lista, key=len)
    return lista

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = lyhin(lista)
    print(tulos)