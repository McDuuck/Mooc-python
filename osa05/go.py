

def kumpi_voitti(pelilauta: list):
    eka = 0
    toka = 0
    for rivi in pelilauta:
        for ruutu in rivi:
            if ruutu == 1:
                eka += 1
            if ruutu == 2:
                toka += 1
    if eka > toka:
        arvo = 1
    if toka > eka:
        arvo = 2
    if eka == toka:
        arvo = 0
    print(arvo)
    return arvo
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]    
    kumpi_voitti(m)
