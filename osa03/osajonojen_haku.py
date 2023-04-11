sana = input("Sana: ")
merkki = input("Merkki: ")
n1 = sana.find(merkki)
n3 = n1 +3
    


if n3 in range(len(sana)):
    print(sana[n1:n3])
    
    
    
   
#osa 2
sana = input("Sana: ")
merkki = input("Merkki: ")
n1 = sana.find(merkki)
n3 = n1 +3


while True:    
    if len(sana) == 0:
        break
    if n3 in range(len(sana)):
        print(sana[n1:n3])
    n1 += 1
    