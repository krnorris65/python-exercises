from movements import IFly

class Parakeet(IFly):
    def __init__(self):
        IFly.__init__(self)
        self.maximum_height = 50
    
    def __str__(self):
        return "Parakeet"