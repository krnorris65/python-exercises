from movements import IMove

class Gerbil(IMove):
    def __init__(self):
        IMove.__init__(self)

    def __str__(self):
        return "Gerbil"