# TEE RATKAISUSI TÄHÄN:
class Auto:
    def __init__(self):
        self.__tankki = 0
        self.__matka = 0
        
    def tankkaa(self):
        self.__tankki = 60
        

    def aja(self, km: int):
        if km <= self.__tankki:
            self.__tankki -= km
            self.__matka += km
        else:
            self.__matka += self.__tankki
            self.__tankki = 0
    
    
    def __str__(self):
        return f'Auto: ajettu {self.__matka} km, bensaa {self.__tankki} litraa'

if __name__ == "__main__":
    auto = Auto()
    auto.tankkaa
    auto.aja(10)
    auto.aja(20)
    auto.aja(10)
    auto.aja(20)
    auto.aja(5)
    print(auto)