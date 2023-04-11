# tee ratkaisu tänne
def lista_tahtina(list):
    n1 = 0
    while n1 in range(len(list)):
        print("*" * list[n1])
        n1 += 1

if __name__ == "__main__":
    lista_tahtina([3,7,1,1,2])

