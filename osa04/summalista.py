# tee ratkaisu tänne
def summa(a, b):
    n1 = 0
    lista = []
    while n1 < len(b):
        summa = a[n1] + b[n1]
        lista.append(summa)
        n1 += 1
        
    return lista
        




if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b))
    