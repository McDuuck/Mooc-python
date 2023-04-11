# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def luvuista_suurin(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if a == b and a > c and b > c:
        return a
    else:
        return c


if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)