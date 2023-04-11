import random

def sanat(n: int, alku: str):
    sanat_lista = []
    seen_words = set()
    with open("sanat.txt", "r") as f:
        for line in f:
            word = line.strip()
            if word not in seen_words:
                if word.startswith(alku):
                    sanat_lista.append(word)
                    seen_words.add(word)
    if n > len(sanat_lista):
        raise ValueError
    random_words = random.sample(sanat_lista, n)
    return random_words


if __name__ == "__main__":
    lista = sanat(3, "ca")
    for sana in lista:
        print(sana)
