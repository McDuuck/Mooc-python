def tulosta(sudoku: list):

    rivi = 0
    ruutu = 0
    for n1 in range(9):
        for n2 in range(9):
            if sudoku[n1][n2] == 0:
                sudoku[n1][n2] = "_"
    
    uus = sudoku[:]

    for rivi in range(9):
        if rivi > 0 and rivi % 3 == 0:
            print()
    
        for ruutu in range(9):
            print(uus[rivi][ruutu], end=" ")
            if (ruutu +1) % 3 == 0:
                print(end=" ")

        print()


def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    sudoku[rivi_nro][sarake_nro] = luku



if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)