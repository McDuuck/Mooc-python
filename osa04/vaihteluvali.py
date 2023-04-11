# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def vaihteluvali(lista: list):
    vaihteluvali = max(lista) - min(lista)
    return vaihteluvali


if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)