from .flower import Flower
from attributes import INotOrganic

class Rose(Flower, INotOrganic):
    def __init__(self):
        super().__init__()
        INotOrganic.__init__(self)
    
    def __str__(self):
        return "Rose"