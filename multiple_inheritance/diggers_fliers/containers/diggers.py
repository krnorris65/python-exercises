from movements import IDig

class Diggers:
    def __init__(self):
        self.__animals = []
    
    def add_animal(self, animal):
        if isinstance(animal, IDig):
            self.__animals.append(animal)
        else:
            print(f"{animal} is not a digger")

    @property
    def animals(self):
        return self.__animals