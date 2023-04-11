# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def viiva(x, y):
    if y == "":
        print("*" * x)
    else:
        print(y[0] * x)
    
def kuvio(eka, toka, kolmas, neljas):
    numero = 0
    while numero < eka:
        numero += 1
        viiva(numero, toka)
    n1 = 0
    while n1 < kolmas:
        n1 += 1
        viiva(eka, neljas)


if __name__ == "__main__":
    kuvio(5, "x", 2, "o")

    
