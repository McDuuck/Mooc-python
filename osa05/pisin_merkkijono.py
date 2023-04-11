def pisin(merkkijonot: list):
    pisin = sorted(merkkijonot, key=len)
    pisin = pisin[-1]
    return pisin





if __name__ == "__main__":
    jonot = ["ab", "a"]
    print(pisin(jonot))