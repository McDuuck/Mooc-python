def poista_isot(lista):
    for c in lista:
        if c.isupper():
            lista.remove(c)
    for a in lista:
        if a.isupper():
            lista.remove(a)
    for b in lista:
        if b.isupper():
            lista.remove(b)        
    return lista
    



if __name__ == "__main__":
    lista = ['aaaa', 'BBBB', 'CCCC', 'DDDD', 'EEEE', 'ffff', 'GGGG', 'HHHH']
    #lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)