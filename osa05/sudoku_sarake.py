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
        
    


if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sarake_oikein(sudoku, 4))
    