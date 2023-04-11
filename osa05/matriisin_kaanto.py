def transponoi(matriisi: list):
    for eka in range(len(matriisi)):
        for toka in range(eka, len(matriisi)):
            uus = matriisi[eka][toka]
            matriisi[eka][toka] = matriisi[toka][eka]
            matriisi[toka][eka] = uus



if __name__ == "__main__":
    matriisi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matriisi)
    transponoi(matriisi)
    print(matriisi)