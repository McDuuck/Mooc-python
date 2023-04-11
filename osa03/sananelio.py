# tee ratkaisu tänne
def nelio(x, y):
    lista = []
    n1 = 0
    for i in x:
        lista += i
    for a in range(y):
        for b in range(y):
            i = lista[n1]
            print(i, end=(''))
            n1 += 1
            if n1 == len(lista):
                n1 = 0
        print()
            
    

if __name__ == "__main__":
    nelio("ab", 3)

