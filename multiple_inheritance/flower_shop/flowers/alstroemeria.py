from .flower import Flower
from attributes import INotOrganic

class Alstroemeria(Flower, INotOrganic):
    def __init__(self):
        Flower.__init__(self)
        INotOrganic.__init__(self)
    
    def __str__(self):
        return "Alstroemeria"