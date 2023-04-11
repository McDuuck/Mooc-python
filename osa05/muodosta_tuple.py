def tee_tuple(x: int, y: int, z: int):
    lista = (x, y, z)
    lista = tuple(sorted(lista))
    
    x = lista[0]
    y = lista[2]
    z = sum(lista)
    return x, y, z





if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))