# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!

def palindromi(lista):
    return lista == lista[::-1]

def main():
    while True:
        sana = input("Anna palindromi: ")
        if palindromi(sana):
            print(sana, "on palindromi!")
            break
        
        print("ei ollut palindromi")
            

main()
    
    
        
        
   
        

