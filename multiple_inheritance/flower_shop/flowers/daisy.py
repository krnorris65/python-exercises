from .flower import Flower
from attributes import IOrganic

class Daisy(Flower, IOrganic):
    def __init__(self):
        super().__init__()
        IOrganic.__init__(self)
    
    def __str__(self):
        return "Daisy"