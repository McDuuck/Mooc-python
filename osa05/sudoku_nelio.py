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


