nimi = input("Kenelle teos omistetaan: ")
tiedot = input("Mihin kirjoitetaan: ")
with open(tiedot, "w") as tiedosto:
    tiedosto.write(str(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi"))
