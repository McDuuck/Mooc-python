while True:
    print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    komento = int(input("Valinta: "))
    
    if komento == 1:
        with open("paivakirja.txt", "a") as tiedosto:
            merkki = input("Anna merkintä: ")
            tiedosto.write(f"{merkki}\n")
            print("Päiväkirja tallennettu")
    
    if komento == 2:
        with open("paivakirja.txt") as tiedosto:
            print("Merkinnät:")
            for rivi in tiedosto:
                print(rivi)


    if komento == 0:
        print("Heippa!")
        break
