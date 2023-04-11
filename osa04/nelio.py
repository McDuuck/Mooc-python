# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(x, y):
    if y == "":
        print("*" * x)
    else:
        print(y[0] * x)

def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    toinen = koko
    while koko > 0:
        viiva(toinen, merkki)
        koko -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "+")
