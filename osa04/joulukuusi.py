# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def joulukuusi(x):
    print("joulukuusi!")
    n1 = x
    tahti = "*"
    vali = " "
    while n1 > 0:
        n1 -= 1
        print(" " * n1 + tahti)
        tahti += "**"
    x = x -1
    print(" " * x + "*")


if __name__ == "__main__":
    joulukuusi(3)