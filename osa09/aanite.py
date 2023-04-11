# TEE RATKAISUSI TÄHÄN:
class Aanite:
    def __init__(self, pituus: int):
        if pituus < 0:
            raise ValueError
        self.__pituus = pituus
    
    @property
    def pituus(self):
        return self.__pituus
    
    @pituus.setter
    def pituus(self, uus: int):
        if uus < 0:
            raise ValueError
        else: 
            self.__pituus = uus

if __name__ == "__main__":
    the_wall = Aanite(43)
    print(the_wall.pituus)
    the_wall.pituus = 44
    print(the_wall.pituus)


