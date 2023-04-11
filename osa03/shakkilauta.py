# tee ratkaisu tänne
# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
def shakkilauta(x):
    for r in range(x):
        for c in range(x):
            print(int((c + r + 1) % 2), end="")
        print()
if __name__ == "__main__":
    shakkilauta(3)
