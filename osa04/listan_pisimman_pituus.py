# tee ratkaisu tänne
def pisimman_pituus(lista):
    lista = max(lista, key=len)
    lista = len(lista)
    return lista



if __name__ == "__main__":
    lista = ["Arto", "Matti"]
    tulos = pisimman_pituus(lista)
    print(tulos)