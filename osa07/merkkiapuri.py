from string import punctuation
def vaihda_koko(merkkijono: str):
    sana = ''
    for i in merkkijono:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        sana += i
    return sana

def puolita(merkkijono: str):
    pituus = len(merkkijono) // 2
    ab = merkkijono[:pituus]
    ba = merkkijono[pituus:]

    return ab, ba

def poista_erikoismerkit(merkkijono: str):
    for i in merkkijono:
        if i in punctuation or i == "¤":
            merkkijono = merkkijono.replace(i, '')

    return merkkijono

if __name__ == '__main__':
    mjono = "Moi kaikki!1!"
    print(vaihda_koko(mjono))
    p1, p2 = puolita(mjono)
    print(p1)
    print(p2)

    m2 = poista_erikoismerkit("a,b.c;d:e_f*g!h#i¤j%k&l/m(n)")
    print(m2)