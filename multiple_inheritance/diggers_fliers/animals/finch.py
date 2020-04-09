from movements import IFly

class Finch(IFly):
    def __init__(self):
        IFly.__init__(self)
        self.maximum_height = 70
    
    def __str__(self):
        return "Finch"