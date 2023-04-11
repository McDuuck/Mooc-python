# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(x, y):
    if y == "":
        print("*" * x)
    else:
        print(y[0] * x)

def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    toinen = 0
    while toinen < koko:
        toinen += 1
        viiva(toinen, "#")


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
