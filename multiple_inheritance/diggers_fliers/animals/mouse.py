from movements import IMove

class Mouse(IMove):
    def __init__(self):
        IMove.__init__(self)

    def __str__(self):
        return "Mouse"