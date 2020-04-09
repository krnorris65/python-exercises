from movements import IMove, IDig

class Ant(IMove, IDig):
    def __init__(self):
        IMove.__init__(self)
        IDig.__init__(self)
    
    def __str__(self):
        return "Ant"