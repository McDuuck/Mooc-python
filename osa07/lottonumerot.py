from random import shuffle
def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    lista = list(range(alaraja, ylaraja))
    shuffle(lista)
    numerot = lista[0:maara]
    numerot.sort()
    return numerot

if __name__ == "__main__":
    for numero in lottonumerot(7, 1, 40):
        print(numero)