# tee ratkaisu tänne
def parilliset(lista):
    uusi_lista = [n for n in lista if n % 2 == 0]
    return uusi_lista


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)