from .flower import Flower
from attributes import INotOrganic

class Rose(Flower, INotOrganic):
    def __init__(self):
        Flower.__init__(self)
        INotOrganic.__init__(self)
    
    def __str__(self):
        return "Rose"