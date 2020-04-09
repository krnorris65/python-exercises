from movements import IFly

class Fliers:
    def __init__(self):
        self.__animals = []
    
    def add_animal(self, animal):
        if isinstance(animal, IFly):
            self.__animals.append(animal)
        else:
            print(f"{animal} is not a flier")
            
    @property
    def animals(self):
        return self.__animals