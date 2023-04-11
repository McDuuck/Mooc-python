lista = []
with open("wordlist.txt") as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        lista.append(rivi)
    
lause = input("Write text: ")
lause = lause.split()

testi = []
for sana in lause:
    if sana.lower() in lista:
        testi.append(sana)

    else:
        sana = sana.replace(sana, f"*{sana}*")
        testi.append(sana)

for i in testi:
    print(i, end=" ")