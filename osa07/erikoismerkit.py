import string

def jaa_merkkeihin(merkkijono: str):
    eka = ''
    toka = ''
    kolmas = ''
    for kirjain in merkkijono:
        if kirjain in string.ascii_letters:
            eka += kirjain
        elif kirjain in string.punctuation:
            toka += kirjain
        else:
            kolmas += kirjain

    return (eka, toka, kolmas)

if __name__ == "__main__":

    osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(osat[0])
    print(osat[1])
    print(osat[2])