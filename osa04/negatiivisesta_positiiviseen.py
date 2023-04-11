# Kirjoita ratkaisu tähän
luku = int(input("Anna luku: "))
for luku in range(-luku, luku+1):
    if luku == 0:
        continue
    print(luku)
