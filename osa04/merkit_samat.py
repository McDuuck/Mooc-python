# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def samat(a, b, c):
    if b not in range(len(a)):
        return False
    if c not in range(len(a)):
        return False
    if a[b] == a[c]:
        return True
    else:
        return False
    
    

if __name__ == "__main__":
    print(samat("koodari", 1, 2))
    