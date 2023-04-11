def hae(lista):
    nimi = input("nimi: ")
    if nimi in lista:
        print(lista[nimi])
    if nimi not in lista:
        print("ei numeroa")

def lisaa(lista):
    nimi = input("nimi: ")
    numero = input("numero: ")
    lista[nimi] = numero
    print("ok!")

def main():
    lista = {}
    while True:
        komento = int(input("komento, (1 hae, 2 lisää, 3 lopeta): "))
        if komento == 3:
            break
        if komento == 2:
            lisaa(lista)
        if komento == 1:
            hae(lista)
    print("lopetetaan...")
    
main()