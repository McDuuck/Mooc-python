from fractions import Fraction

def jaa_palasiksi(maara: int):
    osat = []
    for n1 in range(maara):
        osat.append(Fraction(1, maara))

    return osat

if __name__ == "__main__":
    for p in jaa_palasiksi(3):
        print(p)