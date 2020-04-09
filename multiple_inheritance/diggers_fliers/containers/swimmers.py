from movements import ISwim
class Swimmers:
    def __init__(self):
        self.__animals = []
    
    def add_animal(self, animal):
        if isinstance(animal, ISwim):
            self.__animals.append(animal)
        else:
            print(f"{animal} is not a swimmer")
    @property
    def animals(self):
        return self.__animals