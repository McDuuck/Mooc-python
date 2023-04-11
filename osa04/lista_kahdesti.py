lista = []
while True:
    luku = int(input("Anna luku: "))
    lista.append(luku)

    
    
    if luku == 0:
        break
    
    print(f"Lista: {lista}")
    print(f"Järjestettynä: {sorted(lista)}")
    
print("Moi!")


