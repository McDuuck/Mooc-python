import math

while True:
    luku = int(input("Anna luku: "))
    if luku > 0:
        kertoma = math.factorial(luku)
        print(f"Luvun {luku} kertoma on {kertoma}")
    if luku <= 0:
        break
print("Kiitos ja moi!")



