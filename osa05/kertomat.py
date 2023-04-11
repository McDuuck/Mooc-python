def kertomat(n: int):
    lista = {}
    n1 = 1
    
    for kerto in range(1, n +1):
        n1 *= kerto
        lista[kerto] = n1
    return lista






if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])