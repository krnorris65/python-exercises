from movements import ISwim, IMove

class Terrapin(ISwim, IMove):
    def __init__(self):
        ISwim.__init__(self)
        IMove.__init__(self)
        self.maximum_depth = 20
    
    def __str__(self):
        return "Terrapin"