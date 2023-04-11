# tee ratkaisu tähän
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def tulosta_monesti(x, y):
    n1 = 0
    while n1 < y:
        n1 += 1
        print(x)

if __name__ == "__main__":
    tulosta_monesti("python", 5)