# tee ratkaisu tänne
def positiivisten_summa(lista):
    lista = [n for n in lista if n > 0]
    lista = sum(lista)
    return lista
    


if __name__ == "__main__":
    lista = [1,-2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)

