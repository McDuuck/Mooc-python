sana = input("Sana: ")
merkki = input("Merkki: ")
n1 = 0

while n1 < len(sana)-2:
    if sana[n1] == merkki:
        print(sana[n1:n1+3])
    n1 += 1
        
    