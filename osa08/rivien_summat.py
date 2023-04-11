def rivien_summat(matriisi: list):
    n1 = 0
    while n1 in range(len(matriisi)):
        summa = sum(matriisi[n1])
        matriisi[n1].append(summa)
        n1 += 1


if __name__ == "__main__":
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)