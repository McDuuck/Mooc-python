import random
import string
def luo_salasana(maara: int):
    salasana = random.choices(string.ascii_lowercase, k=maara)

    return ''.join(salasana)

if __name__ == "__main__":
    sala = luo_salasana(6)
    print(sala)