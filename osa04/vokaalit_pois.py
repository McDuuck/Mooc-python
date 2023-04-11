import re
def ilman_vokaaleja(mjono):
    mjono = re.sub('[aeiouyäöå]', '', mjono)
    return mjono



if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))
    #"a", "e", "i", "o", "u", "y", "ä", "ö"