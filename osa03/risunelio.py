# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def risunelio(pituus):
    n1 = 0
    while n1 < pituus:
        print("#" * pituus)
        n1 += 1
if __name__ == "__main__":
    risunelio(5)