# Kirjoita ratkaisu tähän
lista = [1, 2, 3, 4, 5]
while True:
    indexi = int(input("Anna indeksi: "))
    if indexi == -1:
        break
    arvo = int(input("Anna arvo: "))
    lista[indexi] = arvo
    print(lista)
