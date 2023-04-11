def histogrammi(lista):
    tahti = "*"
    maara = {}
    for kerta in lista:
        if kerta not in maara:
            maara[kerta] = 0
        maara[kerta] += 1
    for avain, arvo in maara.items():
        print(f"{avain} {tahti * arvo}")





if __name__ == "__main__":
    histogrammi("abba")