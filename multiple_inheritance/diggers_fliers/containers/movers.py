from movements import IMove

class Movers:
    def __init__(self):
        self.__animals = []
    
    def add_animal(self, animal):
        if isinstance(animal, IMove):
            self.__animals.append(animal)
        else:
            print(f"{animal} is not a ground mover")
    
    @property
    def animals(self):
        return self.__animals