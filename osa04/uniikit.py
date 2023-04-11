# tee ratkaisu tänne
def uniikit(lista):
    lista = sorted(lista)
    return list(dict.fromkeys(lista))



if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))