def eniten_kirjainta(mjono):
    jono = max(set(mjono), key=mjono.count)
    return jono





if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))