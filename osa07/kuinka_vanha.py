from datetime import datetime

tuhat = datetime(1999, 12, 31)
paiva = int(input("Päivä: "))
kuu = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))
ika = datetime(vuosi, kuu, paiva)

erotus = tuhat - ika
if ika < tuhat:
    print(f"Olit {erotus.days} päivää vanha, kun vuosituhat vaihtui.")
else:
    print("Et ollut syntynyt, kun vuosituhat vaihtui.")
