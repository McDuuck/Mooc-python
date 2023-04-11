# tee ratkaisu tänne
def rivi_oikein(sudoku: list, rivi_nro: int):
    n1 = sudoku[rivi_nro]
    lista = []
    for ruutu in n1:
        if ruutu != 0:
            lista.append(ruutu)
    if len(lista) == len(set(lista)):
        return True
    else:
        return False

def sarake_oikein(sudoku: list, sarake_nro: int):
    n2 = 0
    lista = []
    while n2 in range(len(sudoku)):
        n1 = sudoku[n2][sarake_nro]
        if n1 != 0:
            lista.append(n1)
        n2 += 1
        
    if len(lista) == len(set(lista)):
        return True
    else:
        return False

def nelio_oikein(sudoku: list, rivi: int, sarake: int):
    n2 = 0
    n3 = sarake
    lista = []
    while n2 < 3:
        n1 = sudoku[rivi][n3]
        if n1 != 0:
            lista.append(n1)
        n3 += 1
        n2 += 1
    n3 = sarake
    n2 = 0
    while n2 < 3:
        n1 = sudoku[rivi+1][n3]
        if n1 != 0:
            lista.append(n1)
        n3 += 1
        n2 += 1
    n3 = sarake
    n2 = 0
    while n2 < 3:
        n1 = sudoku[rivi+2][n3]
        if n1 != 0:
            lista.append(n1)
        n3 += 1
        n2 += 1
    
    if len(lista) == len(set(lista)):
        return True
    else:
        return False

def sudoku_oikein(sudoku: list):
    for i in range(0, 7, 3):
        for x in range(0, 7, 3):
            if not nelio_oikein(sudoku, i, x):
                return False
    for i in range(9):
        if not (rivi_oikein(sudoku, i) and sarake_oikein(sudoku, i)):
            return False

    return True

if __name__ == "__main__":
    
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    print(sudoku_oikein(sudoku))

    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(sudoku_oikein(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku2))