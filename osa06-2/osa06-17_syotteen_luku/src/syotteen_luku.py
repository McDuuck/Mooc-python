def lue(maara, x, y):
    while True:
        try:
            maara = int(input("syötä luku: "))
            
            if maara >= x and maara <= y:
                return maara

        except ValueError:
            pass
        print(f"Syötteen on oltava kokonaisluku väliltä {x}...{y}")

if __name__ == "__main__":
    luku = lue("syötä luku: ", 5, 10)
    print("syötit luvun:", luku)
